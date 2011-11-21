#------------------------------------------------------------------------------
# Copyright (C) 2007 Riverbank Computing Limited
# Copyright (C) 2011 Richard Lincoln
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------

# Major package imports.

# Enthought library imports.
from pyface.resource.api import ResourceFactory


class PyfaceResourceFactory(ResourceFactory):
    """ The implementation of a shared resource manager. """

    ###########################################################################
    # 'ResourceFactory' interface.
    ###########################################################################

    def image_from_file(self, filename):
        """ Creates an image from the data in the specified filename. """

        # Although QPixmap can load SVG directly, it does not respect the
        # default size, so we use a QSvgRenderer to get the default size.
        if filename.endswith(('.svg', '.SVG')):
            renderer = QtSvg.QSvgRenderer(filename)
            pixmap = QtGui.QPixmap(renderer.defaultSize())
            pixmap.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(pixmap)
            renderer.render(painter)

        else:
            pixmap = QtGui.QPixmap(filename)

        return pixmap

    def image_from_data(self, data, filename=None):
        """ Creates an image from the specified data. """

        image = QtGui.QPixmap()
        image.loadFromData(data)

        return image

#### EOF ######################################################################
