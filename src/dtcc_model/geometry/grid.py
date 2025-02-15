# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

from dataclasses import dataclass
from typing import Union
import numpy as np


from .geometry import Geometry
from dtcc_model import dtcc_pb2 as proto


@dataclass
class Grid(Geometry):
    """Represents a structured quadrilateral grid in 2D.

    Attributes
    ----------
    width : int
        The number of cells in the horizontal direction.
    height : int
        The number of cells in the vertical direction.
    xstep : float
        The horizontal distance between adjacent grid points.
    ystep : float
        The vertical distance between adjacent grid points.

    """

    width: int = 0
    height: int = 0
    xstep: float = 0.0
    ystep: float = 0.0

    def __str__(self):
        return (
            f"DTCC Grid on {self.bounds.bndstr} with {self.width} x {self.height} cells"
        )

    @property
    def num_vertices(self) -> int:
        """Calculate the total number of vertices in the grid.

        Returns
        -------
        int
            The total number of vertices in the grid, including boundary vertices.

        """
        return (self.width + 1) * (self.height + 1)

    @property
    def num_cells(self) -> int:
        """Calculate the total number of cells in the grid.

        Returns
        -------
        int
            The total number of cells in the grid.

        """
        return self.width * self.height

    def from_proto(self, pb: Union[proto.Mesh, bytes]):
        """Initialize the Grid object from a Protocol Buffers message.

        This method populates the Grid object's attributes based on the
        information in a Protocol Buffers message.

        Parameters
        ----------
        pb : Union[proto.Mesh, bytes]
            The Protocol Buffers message or its serialized bytes representation.

        """
        if isinstance(pb, bytes):
            pb = proto.Grid.FromString(pb)
        self.bounds.from_proto(pb.bounds)
        self.width = pb.width
        self.height = pb.height
        self.xstep = pb.xstep
        self.ystep = pb.ystep

    def to_proto(self) -> proto.Mesh:
        """Convert the Grid object to a Protocol Buffers message.

        Returns
        -------
        proto.Mesh
            A Protocol Buffers message representing the Grid object.

        """
        pb = proto.Mesh()
        pb.bounds.CopyFrom(self.bounds.to_proto())
        pb.width = self.width
        pb.height = self.height
        pb.xstep = self.xstep
        pb.ystep = self.ystep
        return pb
