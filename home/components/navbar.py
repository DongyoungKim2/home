"""UI and logic for the navbar component."""

import pynecone as pc

from home import constants, styles
from home.base_state import State
from home.components.logo import logo

# from home.pages.index import index


class NavbarState(State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    search_input: str = ""

    def toggle_sidebar(self):
        """Toggle the sidebar open state."""
        self.sidebar_open = not self.sidebar_open


# Styles to use for the navbar.
logo_style = {
    "width": "3.21em",
    "height": "3em",
}
logo = logo(**logo_style)

button_style = {
    "color": styles.DOC_REG_TEXT_COLOR,
    "_hover": {"color": styles.ACCENT_COLOR, "text_decoration": "none"},
}


def navbar(sidebar: pc.Component = None) -> pc.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """
    # If the sidebar is not provided, create a default one.

    # Create the navbar component.
    return pc.box(
        pc.hstack(
            pc.link(
                pc.hstack(
                    pc.tablet_and_desktop(
                        pc.text(
                            "DONGYOUNG KIM, Ph.D.",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=100,
                            font_color=styles.ACCENT_COLOR_LIGHT,
                        ),
                    ),
                    spacing="0.25em",
                ),
                href="/",
                _hover={"text_decoration": "none"},
            ),

            justify="space-between",
            padding_x=styles.PADDING_X,
        ),
        bg="rgba(255,255,255, 0.8)",
        backdrop_filter="blur(6px)",
        padding_y=["0.8em", "0.8em", "0.5em"],
        border_bottom="0.05em solid rgba(100, 116, 139, .1)",
        position="sticky",
        width="100%",
        top="0px",
        z_index="99",
    )
