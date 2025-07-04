"""
Visualization and saving of lattice structures from lattice objects.

Created in 2025-01-16 by Cadart Thomas, University of technology Belfort Montbéliard.
"""
import json
import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Line3DCollection, Poly3DCollection
import matplotlib.colors as mcolors
import plotly.graph_objects as go

from .Cell import Cell
import matplotlib
matplotlib.use('TkAgg')  # Ou 'Qt5Agg', selon ton système


class LatticeUtils:

    def __init__(self, initFig: bool = False):
        if initFig:
            self.initFigure()
        self.fig = None
        self.ax = None
        self.minAxis = None
        self.maxAxis = None
        self.initFig = initFig
        self.axisSet = False

    def initFigure(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.initFig = True

    def _prepareLatticePlotData(self, cells: list["Cell"], deformedForm: bool = False):
        """Prepare lines and node positions for lattice plotting."""
        beamDraw = set()
        lines = []
        nodes = set()

        for cell in cells:
            for beam in cell.beams:
                if beam.radius != 0.0 and beam not in beamDraw:
                    node1 = beam.point1.getDeformedPos() if deformedForm else (
                    beam.point1.x, beam.point1.y, beam.point1.z)
                    node2 = beam.point2.getDeformedPos() if deformedForm else (
                    beam.point2.x, beam.point2.y, beam.point2.z)
                    lines.append([node1, node2])
                    nodes.update([node1, node2])
                    beamDraw.add(beam)

        return lines, nodes

    def _getBeamColor(self, beam, color_palette, beamColor,idxColor, cells,nbRadiusBins):
        # Assign colors based on the selected scheme
        if beamColor == "Material":
            colorBeam = color_palette[beam.material % len(color_palette)]
        elif beamColor == "Type":
            colorBeam = color_palette[beam.type % len(color_palette)]
        elif beamColor == "Radius":
            if beam.radius not in idxColor:
                idxColor.append(beam.radius)
            colorBeam = color_palette[idxColor.index(beam.radius) % len(color_palette)]
        elif beamColor == "RadiusBin":
            dimRadius = len(cells[0].radius)
            # Ensure radii are extracted properly depending on the dimension
            if not idxColor:
                all_radii = sorted({
                    b.radius[dimRadius] if hasattr(b.radius, '__len__') else b.radius
                    for c in cells for b in c.beams if
                    (b.radius[dimRadius] if hasattr(b.radius, '__len__') else b.radius) > 0
                })
                if not all_radii:
                    idxColor = [0.0]
                else:
                    min_r, max_r = min(all_radii), max(all_radii)
                    bin_edges = np.linspace(min_r, max_r, nbRadiusBins + 1)
                    idxColor = bin_edges

            # Get the beam radius at the specified dimension
            radius_value = beam.radius[dimRadius] if hasattr(beam.radius,
                                                             '__len__') else beam.radius
            bin_idx = np.digitize(radius_value, idxColor, right=True) - 1
            colorBeam = color_palette[bin_idx % len(color_palette)]
        else:
            colorBeam = "blue"
        return colorBeam, idxColor

    def _setMinMaxAxis(self, latticeDimDict: dict) -> None:
        limMin = min(latticeDimDict["xMin"], latticeDimDict["yMin"], latticeDimDict["zMin"])
        limMax = max(latticeDimDict["xMax"], latticeDimDict["yMax"], latticeDimDict["zMax"])
        self.minAxis = min(limMin, self.minAxis) if self.minAxis is not None else limMin
        self.maxAxis = max(limMax, self.maxAxis) if self.maxAxis is not None else limMax
        self.axisSet= True

    def visualizeLattice3D(self, cells: list["Cell"], latticeDimDict: dict, beamColor: str = "Material",
                           voxelViz: bool = False, deformedForm: bool = False, nameSave: str = None,
                           plotCellIndex: bool = False, explodeVoxel: float = 0.0, plotting: bool = True,
                           nbRadiusBins: int = 5) -> None:

        """
        Visualizes the lattice in 3D using matplotlib.

        Parameters:
        -----------
        cells: list of Cell
            List of cells to visualize.
        latticeDimDict: dict
            Dictionary containing lattice dimension information (xMin, xMax, yMin, yMax, zMin, zMax).
        beamColor: str, optional (default: "Material")
            Color scheme for beams. Options:
            - "Material": Color by material.
            - "Type": Color by type.
            - "Radius": Color by radius.
        voxelViz: bool, optional (default: False)
            If True, visualize as voxels; otherwise, use beam visualization.
        deformedForm: bool, optional (default: False)
            If True, use deformed node positions.
        nameSave: str, optional
            If provided, save the plot with this name.
        plotCellIndex: bool, optional (default: False)
            If True, plot cell indices.
        """
        if self.initFig is False:
            self.initFigure()

        def generate_colors(n: int) -> list:
            """Generate a list of `n` distinct colors."""
            base_colors = list(mcolors.TABLEAU_COLORS.values())
            if n <= len(base_colors):
                return base_colors[:n]
            return base_colors + list(mcolors.CSS4_COLORS.values())[:n - len(base_colors)]

        self.ax.set_axis_off()

        # Generate a large color palette to avoid missing colors
        max_elements = max(len(cells), 20)  # Dynamically decide the number of colors
        color_palette = generate_colors(max_elements)
        idxColor = []

        if not voxelViz:
            beamDraw = set()
            lines = []
            colors = []
            nodeX, nodeY, nodeZ = [], [], []
            nodeDraw = set()

            for cell in cells:
                for beam in cell.beams:
                    if beam.radius != 0.0:
                        if beam not in beamDraw:
                            colorBeam, idxColor = self._getBeamColor(beam, color_palette, beamColor, idxColor, cells, nbRadiusBins)
                            # Add line data
                            lines, nodes = self._prepareLatticePlotData(cells, deformedForm)
                            colors.append(colorBeam)
                            beamDraw.add(beam)

                        # Add node data
                        for node in nodes:
                            if node not in nodeDraw:
                                nodeDraw.add(node)
                                nodeX.append(node[0])
                                nodeY.append(node[1])
                                nodeZ.append(node[2])

                if plotCellIndex:
                    self.ax.text(cell.centerPoint[0], cell.centerPoint[1], cell.centerPoint[2], str(cell.index),
                            color='black', fontsize=10)

            # Plot lines and nodes
            line_collection = Line3DCollection(lines, colors=colors, linewidths=2)
            self.ax.add_collection3d(line_collection)
            self.ax.scatter(nodeX, nodeY, nodeZ, c='black', s=5)

        else:  # Voxel visualization
            for cell in cells:
                x, y, z = cell.coordinateCell
                dx, dy, dz = cell.cellSize

                if beamColor == "Material":
                    colorCell = color_palette[cell.beams[0].material % len(color_palette)]
                elif beamColor == "Type":
                    colorCell = color_palette[cell.latticeType % len(color_palette)]
                elif beamColor == "Radius":
                    colorCell = cell.getRGBcolorDependingOfRadius()
                else:
                    colorCell = "blue"  # Default color

                x_offset = explodeVoxel * (x - latticeDimDict["xMin"]) / dx
                y_offset = explodeVoxel * (y - latticeDimDict["yMin"]) / dy
                z_offset = explodeVoxel * (z - latticeDimDict["zMin"]) / dz
                self.ax.bar3d(x + x_offset, y + y_offset, z + z_offset,
                         dx, dy, dz, color=colorCell, alpha=0.5, shade=True, edgecolor='k')

        if self.axisSet is False:
            self._setMinMaxAxis(latticeDimDict)

        # Save or show the plot
        if plotting:
            if nameSave is not None:
                plt.savefig(nameSave)
            else:
                self.show()


    def visualizeLattice3D_interactive(self, lattice, beamColor: str = "Material", voxelViz: bool = False,
                                       deformedForm: bool = False, plotCellIndex: bool = False) -> "go.Figure":
        """
        Visualizes the lattice in 3D using Plotly.

        Parameters:
        -----------
        beamColor: string (default: "Material")
            "Material" -> color by material
            "Type" -> color by type
        voxelViz: boolean (default: False)
            True -> voxel visualization
            False -> beam visualization
        deformedForm: boolean (default: False)
            True -> deformed form
        plotCellIndex: boolean (default: False)
            True -> plot the index of each cell
        """

        color_list = ['blue', 'green', 'red', 'yellow', 'orange', 'purple', 'cyan', 'magenta']
        fig = go.Figure()

        if not voxelViz:
            beamDraw = set()
            nodeDraw = set()
            node_coords = []
            node_colors = []
            lines_x = []
            lines_y = []
            lines_z = []
            line_colors = []
            node1 = None
            node2 = None

            for cell in lattice.cells:
                for beam in cell.beams:
                    if beam not in beamDraw:
                        if deformedForm:
                            node1 = beam.point1.getDeformedPos()
                            node2 = beam.point2.getDeformedPos()
                        else:
                            node1 = (beam.point1.x, beam.point1.y, beam.point1.z)
                            node2 = (beam.point2.x, beam.point2.y, beam.point2.z)

                        # Add the beam to the figure
                        lines_x.extend([node1[0], node2[0], None])
                        lines_y.extend([node1[1], node2[1], None])
                        lines_z.extend([node1[2], node2[2], None])

                        # Determine the color of the beam
                        if beamColor == "Material":
                            colorBeam = color_list[beam.material % len(color_list)]
                        elif beamColor == "Type":
                            colorBeam = color_list[beam.type % len(color_list)]
                        else:
                            colorBeam = 'grey'

                        line_colors.extend([colorBeam, colorBeam, colorBeam])

                        beamDraw.add(beam)

                    # Add the nodes to the figure
                    for node in [node1, node2]:
                        if node not in nodeDraw:
                            node_coords.append(node)
                            nodeDraw.add(node)
                            # Determine the color of the node
                            node_colors.append('black')

                if plotCellIndex:
                    cell_center = cell.centerPoint
                    fig.add_trace(go.Scatter3d(
                        x=[cell_center[0]],
                        y=[cell_center[1]],
                        z=[cell_center[2]],
                        mode='text',
                        text=str(cell.index),
                        textposition="top center",
                        showlegend=False
                    ))

            # Add the beams to the figure
            fig.add_trace(go.Scatter3d(
                x=lines_x,
                y=lines_y,
                z=lines_z,
                mode='lines',
                line=dict(color=line_colors, width=5),
                hoverinfo='none',
                showlegend=False
            ))

            # Add the nodes to the figure
            if node_coords:
                node_x, node_y, node_z = zip(*node_coords)
                fig.add_trace(go.Scatter3d(
                    x=node_x,
                    y=node_y,
                    z=node_z,
                    mode='markers',
                    marker=dict(size=4, color=node_colors),
                    hoverinfo='none',
                    showlegend=False
                ))

        else:
            # Vizualize the lattice as a voxel grid
            for cell in lattice.cells:
                x, y, z = cell.coordinateCell
                dx, dy, dz = cell.cellSize

                if beamColor == "Material":
                    colorCell = color_list[cell.beams[0].material % len(color_list)]
                elif beamColor == "Type":
                    colorCell = color_list[int(str(cell.latticeType)[0]) % len(color_list)]
                else:
                    colorCell = 'grey'

                # Create the voxel
                fig.add_trace(go.Mesh3d(
                    x=[x, x + dx, x + dx, x, x, x + dx, x + dx, x],
                    y=[y, y, y + dy, y + dy, y, y, y + dy, y + dy],
                    z=[z, z, z, z, z + dz, z + dz, z + dz, z + dz],
                    color=colorCell,
                    opacity=0.5,
                    showlegend=False
                ))

        # Configure the layout
        limMin = min(lattice.xMin, lattice.yMin, lattice.zMin)
        limMax = max(lattice.xMax, lattice.yMax, lattice.zMax)
        fig.update_layout(
            scene=dict(
                xaxis=dict(title='X', range=[limMin, limMax], backgroundcolor='white', showgrid=True, zeroline=True),
                yaxis=dict(title='Y', range=[limMin, limMax], backgroundcolor='white', showgrid=True, zeroline=True),
                zaxis=dict(title='Z', range=[limMin, limMax], backgroundcolor='white', showgrid=True, zeroline=True),
                aspectmode='cube'
            ),
            margin=dict(l=0, r=0, b=0, t=0),
            showlegend=False
        )

        return fig  # Return the figure


    def visualCellZoneBlocker(self, lattice, erasedParts: list[tuple]) -> None:
        """
        Visualize the lattice with erased parts

        Parameters:
        -----------
        erasedParts: list of tuple
            List of erased parts with (x_start, y_start, z_start, x_dim, y_dim
        """

        # Plot global lattice cube
        x_max = lattice.xMax
        y_max = lattice.yMax
        z_max = lattice.zMax
        vertices_global = [[0, 0, 0], [x_max, 0, 0], [x_max, y_max, 0], [0, y_max, 0],
                           [0, 0, z_max], [x_max, 0, z_max], [x_max, y_max, z_max], [0, y_max, z_max]]
        self.ax.add_collection3d(
            Poly3DCollection([vertices_global], facecolors='grey', linewidths=1, edgecolors='black', alpha=0.3))

        # Plot erased region cube
        for erased in erasedParts:
            x_start, y_start, z_start, x_dim, y_dim, z_dim = erased
            vertices_erased = [[x_start, y_start, z_start], [x_start + x_dim, y_start, z_start],
                               [x_start + x_dim, y_start + y_dim, z_start], [x_start, y_start + y_dim, z_start],
                               [x_start, y_start, z_start + z_dim], [x_start + x_dim, y_start, z_start + z_dim],
                               [x_start + x_dim, y_start + y_dim, z_start + z_dim],
                               [x_start, y_start + y_dim, z_start + z_dim]]
            self.ax.add_collection3d(
                Poly3DCollection([vertices_erased], facecolors='red', linewidths=1, edgecolors='black', alpha=0.6))

        # Set labels and limits
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_xlim([0, x_max])
        self.ax.set_ylim([0, y_max])
        self.ax.set_zlim([0, z_max])

        plt.show()

    def saveJSONToGrasshopper(self, lattice, nameLattice: str = "LatticeObject", multipleParts: int = 1) -> None:
        """
        Save the current lattice object to JSON files for Grasshopper compatibility, separating by cells.

        Parameters:
        -----------
        lattice: Lattice
            Lattice object to save.
        nameLattice: str
            Name of the lattice file to save.
        multipleParts: int, optional (default: 1)
            Number of parts to save.
        """
        folder = "Saved_Lattice"
        if not os.path.exists(folder):
            os.makedirs(folder)

        numberCell = len(lattice.cells)
        cellsPerPart = max(1, numberCell // multipleParts)

        for partIdx in range(multipleParts):
            partName = f"{nameLattice}_part{partIdx + 1}.json" if multipleParts > 1 else f"{nameLattice}.json"
            file_pathJSON = os.path.join(folder, partName)

            partNodesX = []
            partNodesY = []
            partNodesZ = []
            partRadius = []

            startIdx = partIdx * cellsPerPart
            endIdx = min((partIdx + 1) * cellsPerPart, numberCell)

            for cell in lattice.cells[startIdx:endIdx]:
                for beam in cell.beams:
                    partNodesX.append(beam.point1.x)
                    partNodesX.append(beam.point2.x)
                    partNodesY.append(beam.point1.y)
                    partNodesY.append(beam.point2.y)
                    partNodesZ.append(beam.point1.z)
                    partNodesZ.append(beam.point2.z)
                    partRadius.append(max(beam.radius, 0.015))

            obj = {
                "nodesX": partNodesX,
                "nodesY": partNodesY,
                "nodesZ": partNodesZ,
                "radius": partRadius,
                "maxX": lattice.xMax,
                "minX": lattice.xMin,
                "maxY": lattice.yMax,
                "minY": lattice.yMin,
                "maxZ": lattice.zMax,
                "minZ": lattice.zMin,
                "relativeDensity": lattice.getRelativeDensity()
            }

            with open(file_pathJSON, 'w') as f:
                json.dump(obj, f)

            print(f"Saved lattice part {partIdx + 1} to {file_pathJSON}")

    def saveLatticeObject(self, lattice, file_name: str = "LatticeObject") -> None:
        """
        Save the lattice object to a file.

        Parameters:
        -----------
        file_name: str
            Name of the file to save (with or without the '.pkl' extension).
        """
        folder = "Saved_Lattice"
        os.makedirs(folder, exist_ok=True)

        if not file_name.endswith(".pkl"):
            file_name += ".pkl"

        file_path = os.path.join(folder, file_name)

        with open(file_path, "wb") as file:
            pickle.dump(lattice, file)

        print(f"Lattice saved successfully to {file_path}")

    def visualizeMesh(self, meshObject: "MeshObject"):
        mesh = meshObject.mesh
        faces = mesh.vertices[mesh.faces]
        self.ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=0.2, edgecolors='k', alpha=0.2))

        minAxis = min(mesh.bounds[0])
        maxAxis = max(mesh.bounds[1])
        self.minAxis = min(minAxis, self.minAxis) if self.minAxis is not None else minAxis
        self.maxAxis = max(maxAxis, self.maxAxis) if self.maxAxis is not None else maxAxis

    def plotRadiusDistribution(self, cells: list["Cell"], nbRadiusBins: int = 5):
        """
        Plot the radius distribution of beams in the lattice.

        Parameters:
        -----------
        cells: list of Cell
            List of cells to visualize.
        latticeDimDict: dict
            Dictionary containing lattice dimension information (xMin, xMax, yMin, zMin, zMax).
        nbRadiusBins: int
            Number of bins for the histogram.
        """
        all_radii = []
        all_volumes = []

        for cell in cells:
            radius = cell.getRadius()
            if hasattr(radius, '__len__'):
                all_radii.append(radius)
            else:
                all_radii.append([radius])
            all_volumes.append(cell.getVolumeGeomSeparated())

        all_radii = np.array(all_radii)
        dimRadius = all_radii.shape[1]
        all_volumes = np.array(all_volumes)
        sumVolume = np.sum(all_volumes, axis=0)
        ratio_volume = sumVolume / np.sum(sumVolume) * 100

        colors = plt.cm.tab10.colors  # Up to 10 colors predefined

        plt.figure(figsize=(7, 5))
        bins = np.linspace(np.min(all_radii), np.max(all_radii), nbRadiusBins + 1)
        bin_width = (bins[1] - bins[0]) / (dimRadius + 1)

        for i in range(dimRadius):
            shifted_bins = bins[:-1] + i * bin_width
            plt.bar(shifted_bins, np.histogram(all_radii[:, i], bins=bins)[0],
                    width=bin_width, align='edge', color=colors[i % len(colors)], edgecolor='black',
                    label=f'Geometry {i}, Ratio Volume: {ratio_volume[i]:.2f}%')

        plt.title('Radius Distribution')
        plt.xlabel('Radius')
        plt.ylabel('Count')
        plt.legend()
        plt.show()

    def subplotLatticeGeometries(self, cells: list["Cell"], latticeDimDict: dict, nbRadiusBins: int = 5,
                                 explodeVoxel: float = 0.0):
        """
        Create subplots:
        - One subplot per geometry (radius index) with voxel visualization.
        """
        rmin = 0
        rmax = 0.1

        # Determine number of geometries
        dimRadius = len(cells[0].radius) if hasattr(cells[0].radius, '__len__') else 1
        fig, axs = plt.subplots(1, dimRadius, figsize=(5 * dimRadius, 5), subplot_kw={'projection': '3d'})
        axs = [axs] if dimRadius == 1 else axs  # Ensure axs is always iterable
        for ax in axs:
            ax.set_axis_off()


        for rad in range(dimRadius):
            ax = axs[rad]
            for cell in cells:
                x, y, z = cell.coordinateCell
                dx, dy, dz = cell.cellSize

                # Get color based on the radius value for current geometry
                radius = cell.getRadius()
                radius_value = radius[rad] if hasattr(radius, '__len__') else radius
                import matplotlib.cm as cm  # ajouter en haut si pas encore fait

                # Define the colormap from blue to red
                colormap = cm.get_cmap('coolwarm')

                # Normalize radius between 0 and 1
                radius_norm = (radius_value - rmin) / (rmax - rmin)
                radius_norm = np.clip(radius_norm, 0.0, 1.0)
                colorCell = colormap(radius_norm)

                x_offset = explodeVoxel * (x - latticeDimDict["xMin"]) / dx
                y_offset = explodeVoxel * (y - latticeDimDict["yMin"]) / dy
                z_offset = explodeVoxel * (z - latticeDimDict["zMin"]) / dz

                ax.bar3d(x + x_offset, y + y_offset, z + z_offset, dx, dy, dz,
                         color=colorCell, alpha=0.5, shade=True, edgecolor='k')

            if self.axisSet is False:
                self._setMinMaxAxis(latticeDimDict)

            ax.set_title(f'Geometry {rad}')
            ax.set_xlim3d(self.minAxis, self.maxAxis)
            ax.set_ylim3d(self.minAxis, self.maxAxis)
            ax.set_zlim3d(self.minAxis, self.maxAxis)
            ax.set_box_aspect([1, 1, 1])

        plt.tight_layout()
        plt.show()

    def show(self):
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_xlim3d(self.minAxis, self.maxAxis)
        self.ax.set_ylim3d(self.minAxis, self.maxAxis)
        self.ax.set_zlim3d(self.minAxis, self.maxAxis)
        self.ax.set_box_aspect([1, 1, 1])
        plt.show()

