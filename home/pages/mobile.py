# -*- coding: utf-8 -*-

import pynecone as pc
from home.templates import webpage
from home import constants
import pandas as pd
from home.base_state import State
from home.pages import projects


def mobile():
    patenttable = pd.read_csv(constants.PATENTS_URL)
    alist = []
    for i in range(len(patenttable)):
        alist.append([patenttable.iloc[i]["년도"], patenttable.iloc[i]
                     ["특허명"]+" "+patenttable.iloc[i]["특허"]])
    return pc.center(
        pc.vstack(
            pc.vstack(
                pc.box(
                    height="100px",
                    width="100%",
                ),
                pc.vstack(
                    pc.box(
                        pc.text("ARTIFICIAL", font_size="1.5em"),
                        width="100%",
                    ),
                    pc.box(
                        pc.text("INTELLIGENCE", font_size="1.5em"),
                        width="100%",
                    ),
                    pc.box(
                        pc.text("PROFESSIONAL", font_size="1.5em"),
                        width="100%",
                    ),
                    pc.box(
                        pc.text("FOR SCIENCE & ", font_size="1.5em",
                                font_weight=100,),
                        width="100%",
                    ),
                    pc.box(
                        pc.text("INDUSTRY", font_size="1.5em",
                                font_weight=100,),
                        width="100%",
                    ),
                    color="white",
                    width="100%",
                    spacing="-1em",
                    font_size="1.7em",
                    padding_left="10px",
                    _hover={
                        "opacity": 0.7,
                    },
                ),
                pc.vstack(
                    pc.box(
                        pc.box(
                            pc.heading("DONGYOUNG KIM, Ph.D",
                                       font_size="1.7em"),

                            width="100%",
                            padding_left="10px",
                            _hover={
                                "opacity": 0.7,
                            },
                        ),
                        width="100%",
                    ),
                    pc.box(
                        pc.hstack(
                            # pc.text("과학과 산업의 인공지능 전문가", font_weight=100,),

                            pc.avatar(src="/picture.png", size="md"),
                            pc.link(
                                pc.button(
                                    "CV",

                                    background_image="white",
                                    color="#5B42F3",
                                    _hover={
                                        "opacity": 0.85,
                                    },
                                    size="md",
                                ),
                                href=constants.CV_URL,
                                button=True,
                                is_external=True,
                            ),
                            pc.link(
                                pc.button(
                                    "이력서",
                                    href=constants.CV_URL,
                                    background_image="white",
                                    color="#AF40FF",
                                    _hover={
                                        "opacity": 0.85,
                                    },
                                    size="md",
                                ),
                                href=constants.CV_URL,
                                button=True,
                                is_external=True,
                            ),
                            pc.link(
                                pc.button(
                                    "blog",

                                    background_image="white",
                                    color="#5B42F3",
                                    _hover={
                                        "opacity": 0.85,
                                    },
                                    size="md",
                                ),
                                href=constants.BLOG_URL,
                                button=True,
                                is_external=True,
                            ),
                        ),
                        padding_left="10px",
                        height="100px",
                        width="100%",
                        padding_top="10px",

                    ),
                    width="100%",
                    spacing="0.1em",
                    color="white",
                    font_size="1.7em",

                ),
                width="100%",
                spacing="0em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
            ),
            pc.vstack(

                width="100%",
                padding_top="5%",
            ),
            pc.accordion(
                pc.accordion_item(
                    pc.accordion_button(
                        pc.center(
                            pc.accordion_icon(),
                            pc.heading(
                                "EXPERIENCE",
                                font_size="2em",
                            ),
                            width="100%",
                        ),
                        padding_y="0.5em",
                        width="100%",
                        _hover={
                            "color": "gray",
                        },
                    ),
                    pc.accordion_panel(
                        pc.table(
                            pc.thead(
                                pc.tr(
                                    pc.th("Years"),
                                    pc.th("Title"),
                                )
                            ),
                            pc.tbody(
                                pc.tr(
                                    pc.td("2021 - 현재"),
                                    pc.td(
                                        pc.text("KB 국민은행 서울, 대한민국"),
                                        pc.text("금융 AI 센터"),
                                        pc.text(
                                            "OCR Team Leader (General Manager) @ AI Tech", font_size="1.1em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2021 - 2021"),
                                    pc.td(
                                        pc.text("현대자동차 서울, 대한민국"),
                                        pc.text("AIRS Company"),
                                        pc.text(
                                            "Senior Manager @ MCS Lab", font_size="1.1em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2020 - 2021"),
                                    pc.td(
                                        pc.text("삼성생명 서울, 대한민국"),
                                        pc.text(
                                            "Manager @ Data Analytics Lab", font_size="1.1em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2017 - 2019"),
                                    pc.td(
                                        pc.text(
                                            "한국기초과학연구원 (IBS) 울산, 대한민국"),
                                        pc.text("첨단연성물질 연구단"),
                                        pc.text("Postdoctoral researcher",
                                                font_size="1.1em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2012 - 2016"),
                                    pc.td(
                                        pc.text(
                                            "Texas A&M University Texas, U.S.A"),
                                        pc.text("Research Assistant",
                                                font_size="1.1em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2010 - 2012"),
                                    pc.td(
                                        pc.text(
                                            "The University of Southwestern Medical Center Texas, U.S.A."),
                                        pc.text("Research Assistant",
                                                font_size="1.1em"),
                                    ),
                                ),
                            ),
                        )
                    ),
                    width="100%",
                    index=0,
                    padding_bottom="5%",
                    padding_top="5%",
                ),
                pc.accordion_item(
                    pc.accordion_button(
                        pc.center(
                            pc.accordion_icon(),
                            pc.heading(
                                "EDUCATION",
                                font_size="2em",
                            ),
                            width="100%",
                        ),
                        padding_y="0.5em",
                        width="100%",
                        _hover={
                            "color": "gray",
                        },
                    ),
                    pc.accordion_panel(
                        pc.table(
                            pc.thead(
                                pc.tr(
                                    pc.th("Years"),
                                    pc.th("Title"),
                                )
                            ),
                            pc.tbody(
                                pc.tr(
                                    pc.td("2012 - 2016"),
                                    pc.td(
                                        pc.text(
                                            "Texas A&M University Texas, U.S.A."),
                                        pc.text(
                                            "Doctor of Philosophy in Biomedical Engineering", font_size="1.1em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2010 - 2012"),
                                    pc.td(
                                        pc.text(
                                            "The University of Texas at Dallas Texas, U.S.A."),
                                        pc.text(
                                            "Bachelor's degree in Electrical Engineering and Computer Science", font_size="1.1em"),
                                    ),
                                ),
                            ),
                        )
                    ),
                    width="100%",
                    index=1,
                    padding_bottom="5%",
                    padding_top="5%",
                ),
                pc.accordion_item(
                    pc.accordion_button(
                        pc.center(
                            pc.accordion_icon(),
                            pc.heading(
                                "PROJECTS",
                                font_size="2em",
                            ),
                            width="100%",
                        ),
                        padding_y="0.5em",
                        width="100%",
                        _hover={
                            "color": "gray",
                        },
                    ),
                    pc.accordion_panel(
                        pc.box(padding_top="3%"),
                        pc.flex(

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/lvlm.png", on_click=State.right_0),
                                pc.box(padding_top="20px"),
                                pc.text("LVLM",
                                        as_="strong"),
                                pc.text("(2023)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.lvlm(),
                            # -------------------------------------------
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/ocr.png", on_click=State.right_1),
                                pc.box(padding_top="20px"),
                                pc.text("OCR",
                                        as_="strong"),
                                pc.text("Platform",
                                        as_="strong"),
                                pc.text("(2022)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",

                            ),

                            projects.kbaiocr(),
                            # -------------------------------------------
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/ocr_model.png", on_click=State.right_2),
                                pc.box(padding_top="20px"),
                                pc.text("OCR",
                                        as_="strong"),
                                pc.text("Models",
                                        as_="strong"),
                                pc.text("(2022)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.kbaiocrmodel(),
                        ),
                        pc.box(padding_top="8%"),
                        pc.flex(

                            # -------------------------------------------

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/datalake.png", on_click=State.right_3),
                                pc.box(padding_top="20px"),
                                pc.text("Data",
                                        as_="strong"),
                                pc.text("Lake",
                                        as_="strong"),
                                pc.text("(2021)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.datalake(),
                            # -------------------------------------------
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/sliocr.png", on_click=State.right_4),

                                pc.box(padding_top="20px"),
                                pc.text("SLI",
                                        as_="strong"),
                                pc.text("OCR",
                                        as_="strong"),
                                pc.text("(2021)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",

                            ),

                            projects.sliocr(),
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(size="xl", name="G S",
                                          on_click=State.right_5),

                                pc.box(padding_top="20px"),
                                pc.text("Graph",
                                        as_="strong"),
                                pc.text("DB",
                                        as_="strong"),
                                pc.text("(2021)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.graphdb(),
                            width="100%",
                        ),
                        pc.box(padding_top="8%"),
                        pc.flex(
                            # -------------------------------------------


                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/aim.png", on_click=State.right_6),

                                pc.box(padding_top="20px"),
                                pc.text("AIM",
                                        as_="strong"),
                                pc.text("(2019)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",

                            ),

                            projects.aim(),
                            # -------------------------------------------
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/hist.png", on_click=State.right_7),

                                pc.box(padding_top="20px"),
                                pc.text("AI-HIST",
                                        as_="strong"),
                                pc.text("(2020)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.hist(),
                            # -------------------------------------------
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/aitomography.png", on_click=State.right_8),

                                pc.box(padding_top="20px"),
                                pc.text("AI-TM ",
                                        as_="strong"),
                                pc.text("(2020)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.aitomography(),
                            width="100%",
                        ),
                        pc.box(padding_top="8%"),
                        pc.flex(
                            # -------------------------------------------


                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/spinner.png", on_click=State.right_9),

                                pc.box(padding_top="20px"),
                                pc.text("Dx-figet",
                                        as_="strong"),
                                pc.text("(2021)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.spinner(),
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/evident.png", on_click=State.right_10),

                                pc.box(padding_top="20px"),
                                pc.text("EV-IDENT",
                                        as_="strong"),
                                pc.text("(2020)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.evident(),
                            # -------------------------------------------
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/sr.png", on_click=State.right_11),

                                pc.box(padding_top="20px"),
                                pc.text("SRM",
                                        as_="strong"),
                                pc.text("(2016)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.sr(),
                            width="100%",
                        ),
                        pc.box(padding_top="8%"),
                        pc.flex(
                            # -------------------------------------------


                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/rmum.png", on_click=State.right_12),

                                pc.box(padding_top="20px"),
                                pc.text("R-MUM",
                                        as_="strong"),
                                pc.text("(2016)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.rmum(),
                            # -------------------------------------------
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/her23.png", on_click=State.right_13),

                                pc.box(padding_top="20px"),
                                pc.text("HER2/3",
                                        as_="strong"),
                                pc.text("(2016)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.her23(),
                            # -------------------------------------------
                            pc.spacer(),

                            pc.vstack(
                                pc.avatar(
                                    size="xl", src="projects/her2.png", on_click=State.right_14),

                                pc.box(padding_top="20px"),
                                pc.text("HER2",
                                        as_="strong"),
                                pc.text("(2016)"),
                                style={"cursor": "pointer"},
                                spacing="-0.4em",
                            ),

                            projects.her2(),
                            width="100%",
                        ),
                    ),
                    width="100%",
                    index=3,
                    padding_bottom="5%",
                    padding_top="5%",
                ),
                pc.accordion_item(
                    pc.accordion_button(
                        pc.center(
                            pc.accordion_icon(),
                            pc.heading(
                                "AWARDS",
                                font_size="2em",
                            ),
                            width="100%",
                        ),
                        padding_y="0.5em",
                        width="100%",
                        _hover={
                            "color": "gray",
                        },
                    ),
                    pc.accordion_panel(
                        pc.table(
                            pc.thead(
                                pc.tr(
                                    pc.th("Years"),
                                    pc.th("Title"),
                                )
                            ),
                            pc.tbody(
                                pc.tr(
                                    pc.td("2022"),
                                    pc.td(
                                        pc.text(
                                            "한국지능정보시스템학회 추계 학술대회 우수논문상", font_size="1.1em"),
                                        pc.text(
                                            "Deep Learning OCR based document processing platform and its application in financial domain."),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2020"),
                                    pc.td(
                                        pc.text(
                                            "IEEE ICDAR SROIE text localization task 2020 1 위 ", font_size="1.1em"),
                                        pc.text(
                                            "https://rrc.cvc.uab.es/?ch=13&com=evaluation&task=1"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2020"),
                                    pc.td(
                                        pc.text(
                                            "IEEE ICDAR SROIE text recognition task 2020 1 위 ", font_size="1.1em"),
                                        pc.text(
                                            "https://rrc.cvc.uab.es/?ch=13&com=evaluation&task=2"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2018"),
                                    pc.td(
                                        pc.text(
                                            "Shark Tank Competition 1 위  ", font_size="1.1em"),
                                        pc.text(
                                            "The 22nd International Conference On Miniaturized Systems For Chemistry And Life Sciences, Taiwan"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2016"),
                                    pc.td(
                                        pc.text(
                                            "3D single molecule localization microscopy 부문 1 위 ", font_size="1.1em"),
                                        pc.text(
                                            "SMLMS Challenge (EPFL), Swissland"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2014 - 2016"),
                                    pc.td(
                                        pc.text(
                                            "Texas A&M University 연구 장학금, U.S.A.", font_size="1.1em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2011 - 2014"),
                                    pc.td(
                                        pc.text(
                                            "The University of Texas at Dallas 연구 장학금, U.S.A.", font_size="1.1em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2011"),
                                    pc.td(
                                        pc.text(
                                            "Senior Design Project 2 위 ", font_size="1.1em"),
                                        pc.text(
                                            "The University of Texas at Dallas, U.S.A."),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2010 - 2012 	"),
                                    pc.td(
                                        pc.text(
                                            "The University of Texas at Dallas 학사 장학금, U.S.A.", font_size="1.1em"),
                                    ),
                                ),
                            ),
                        )
                    ),
                    width="100%",
                    index=4,
                    padding_bottom="5%",
                    padding_top="5%",
                ),
                pc.accordion_item(
                    pc.accordion_button(
                        pc.center(
                            pc.accordion_icon(),
                            pc.heading(
                                "PATENTS",
                                font_size="2em",
                            ),
                            width="100%",
                        ),
                        padding_y="0.5em",
                        width="100%",
                        _hover={
                            "color": "gray",
                        },
                    ),
                    pc.accordion_panel(

                        pc.data_table(
                            data=pd.DataFrame(
                                alist, columns=["years", "title"]),
                            pagination=True,
                            search=True,
                            sort=True,
                        ),
                    ),
                    width="100%",
                    index=5,
                    padding_bottom="5%",
                    padding_top="5%",
                ),
                pc.accordion_item(
                    pc.accordion_button(
                        pc.center(
                            pc.accordion_icon(),
                            pc.heading(
                                "PAPERS",
                                font_size="2em",
                            ),
                            width="100%",
                        ),
                        padding_y="0.5em",
                        width="100%",
                        _hover={
                            "color": "gray",
                        },
                    ),
                    pc.accordion_panel(
                        pc.data_table(
                            data=pd.read_csv(constants.PAPERS_URL),
                            pagination=True,
                            search=True,
                            sort=True,
                        ),
                    ),
                    width="100%",
                    index=6,
                    padding_bottom="5%",
                    padding_top="5%",
                ),
                allow_multiple=True,
                width="100%",
                default_index=[0, 1, 2, 3, 4, 5, 6],
            ),

            pc.vstack(
                width="100%",
                padding_top="10%",
            ),
            width="100%",
        ),
        width="100%",
    )
