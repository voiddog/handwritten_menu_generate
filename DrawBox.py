# coding: utf-8
from handright import Template, handwrite
from PIL import ImageFont, Image, ImageColor
from typing import *

Margin = tuple


class DrawBox:

    def __init__(
        self,
        font: ImageFont,
        fill: tuple,
        margin: Margin = (0, 0, 0, 0),
        line_spacing: int = 10,
        word_spacing: int = 0,
        line_spacing_sigma: Optional[float] = None,
        font_size_sigma: Optional[float] = None,
        word_spacing_sigma: Optional[float] = None,
        perturb_x_sigma: Optional[float] = None,
        perturb_y_sigma: Optional[float] = None,
        perturb_theta_sigma: float = 0.07
    ):
        super().__init__()
        self.font = font
        self.fill = fill
        self.margin = margin
        self.line_spacing = line_spacing
        self.word_spacing = word_spacing
        self.line_spacing_sigma = line_spacing_sigma
        self.font_size_sigma = font_size_sigma
        self.word_spacing_sigma = word_spacing_sigma
        self.perturb_x_sigma = perturb_x_sigma
        self.perturb_y_sigma = perturb_y_sigma
        self.perturb_theta_sigma = perturb_theta_sigma

    def render(
            self,
            text: str,
    ) -> Image:
        box_size = self._calculateSize(text)
        template = Template(
            background=Image.new(mode="RGBA", size=box_size,
                                 color=ImageColor.getrgb("#ffffff00")),
            font=self.font,
            line_spacing=self.line_spacing,
            word_spacing=self.word_spacing,
            fill=self.fill,
            line_spacing_sigma=self.line_spacing_sigma,
            font_size_sigma=self.font_size_sigma,
            word_spacing_sigma=self.word_spacing_sigma,
            perturb_theta_sigma=self.perturb_theta_sigma,
            perturb_x_sigma=self.perturb_x_sigma,
            perturb_y_sigma=self.perturb_y_sigma,
        )
        images = handwrite(text, template)
        return next(images)

    def _calculateSize(
        self,
        text: str,
    ) -> tuple[int, int]:
        lines = text.splitlines()
        max_len = 0
        for line in lines:
            max_len = max(max_len, len(line))
        return (self.font.size * max_len + self.word_spacing * (max_len - 1)
                , len(line) * (self.line_spacing + self.line_spacing_sigma))
