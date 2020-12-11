class Box:
    def __init__(self, length, width, height, content_density=1):
        self._length = length
        self._width = width
        self._height = height
        self._content_density = content_density  # плотность содержимого

        self._box_volume = self._length * self._width * self._height  # объём
        self._weight = self._box_volume * self._content_density  # вес содержимого
        self._color = None

    # длина
    @property
    def length(self):
        """Length property docs"""
        return self._length

    @length.setter
    def length(self, length):
        self._length = length
    ########################################

    # ширина
    @property
    def width(self):
        """Width property docs"""
        return self._width

    @width.setter
    def width(self, width):
        self._width = width
    ########################################

    # высота
    @property
    def height(self):
        """Height property docs"""
        return self._height

    @height.setter
    def height(self, height):
        self._height = height
    ########################################

    # плотность содержимого (getter + setter + deleter)
    @property
    def content_density(self):
        """Content density property docs"""
        return self._content_density

    @content_density.setter
    def content_density(self, content_density):
        self._content_density = content_density

    @content_density.deleter
    def content_density(self):
        """Приравнивает атрибут content_density к нулю"""
        self._content_density = 0

    ########################################

    # объём
    @property
    def box_volume(self):
        """Box volume property docs"""
        return self._length * self._width * self._height
    ########################################

    # вес содержимого
    @property
    def weight(self):
        """weight property docs"""
        return self._length * self._width * self._height * self._content_density
    ########################################

    # цвет
    @property
    def color(self):
        """Color property docs"""
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @color.deleter
    def color(self):
        """Удаляет атрибут color"""
        del self._color
    ########################################


if __name__ == '__main__':
    m_box = Box(10, 20, 30)
    print(m_box.length, m_box.width, m_box.height, m_box.box_volume, m_box.weight)

    m_box.content_density = 3
    print(m_box.length, m_box.width, m_box.height, m_box.box_volume, m_box.weight)

    m_box.length += 5
    print(m_box.length, m_box.width, m_box.height, m_box.box_volume, m_box.weight)

    m_box.color = '#303030'
    print(m_box.color)

    print('-' * 79)
    print(Box.length.__doc__)
