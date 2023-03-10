import pynecone as pc

from home import styles
from home.components.logo import logo

footer_item_style = {
    "font_family": "Noto Sans KR",
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
            pc.mobile_only(
                pc.vstack(
                    pc.link(
                        pc.hstack(
                            pc.image(src="/green_favicon.png",
                                     width="20px", height="auto"),
                            pc.text("BLOG"),
                        ),
                        href="https://velog.io/@dongyoungkim",
                    ),
                    pc.link(
                        pc.hstack(
                            pc.image(src="/github-mark.png",
                                     width="20px", height="auto"),
                            pc.text("@DongyoungKim2/home"),
                        ),
                        href="https://github.com/DongyoungKim2/home",
                    ),
                    pc.link(
                        pc.hstack(
                            pc.icon(tag="EmailIcon"),
                            pc.text("Dongyoung.kim@me.com "),
                        ),
                        href="mailto:Dongyoung.kim@me.com",
                    ),
                ),
            ),
            pc.tablet_and_desktop(
                pc.hstack(
                    pc.link(
                        pc.hstack(
                            pc.image(src="/green_favicon.png",
                                     width="20px", height="auto"),
                            pc.text("BLOG"),
                        ),
                        href="https://velog.io/@dongyoungkim",
                    ),
                    pc.text(" | "),
                    pc.link(
                        pc.hstack(
                            pc.image(src="/github-mark.png",
                                     width="20px", height="auto"),
                            pc.text("@DongyoungKim2/home"),
                        ),
                        href="https://github.com/DongyoungKim2/home",
                    ),
                    pc.text(" | "),
                    pc.link(
                        pc.hstack(
                            pc.icon(tag="EmailIcon"),
                            pc.text("Dongyoung.kim@me.com "),
                        ),
                        href="mailto:Dongyoung.kim@me.com",
                    ),
                ),
            ),
            pc.link(
                pc.text("Copyright 2023 Dongyoung Kim. Ph.D. "),
                href="http://dongyoungkim.net"
            ),
            width="100%",

        ),
        **style,
    )
