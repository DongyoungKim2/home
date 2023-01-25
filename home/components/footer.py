import pynecone as pc

from home import styles
from home.components.logo import logo

footer_item_style = {
    "font_family": "Inter",
    "font_weight": "500",
    "_hover": {"color": styles.ACCENT_COLOR},
}

footer_style = {
    "box_shadow": "medium-lg",
    "border_top": "0.2em solid #F0F0F0",
    "vertical_align": "bottom",
    "padding_top": "4em",
    "padding_bottom": "2em",
    "padding_x": styles.PADDING_X2,
    "bg": "white",
}


def footer(style=footer_style):
    return pc.box(
        pc.vstack(
            pc.hstack(
                pc.icon(tag="EmailIcon"),
                pc.text("Dongyoung.kim@me.com "),
            ),
            pc.text("Copyright 2023 | Dongyoung Kim. Ph.D. "),
            width="100%",

        ),
        **style,
    )
