# -*- coding: utf-8 -*-

import pynecone as pc
from home.templates import webpage
from home import constants
import pandas as pd
from home.base_state import State
from home.pages import projects


def desktop():
    return pc.center(
        pc.vstack(
            pc.vstack(
                pc.box(
                    height="50px",
                    width="80%",
                ),
                pc.vstack(
                    pc.box(
                        pc.text("ARTIFICIAL", font_size="3em"),
                        width="80%",
                    ),
                    pc.box(
                        pc.text("INTELLIGENCE", font_size="3em"),
                        width="80%",
                    ),
                    pc.box(
                        pc.text("PROFESSIONAL", font_size="3em"),
                        width="80%",
                    ),
                    pc.box(
                        pc.text("FOR SCIENCE & ", font_size="3em",
                                font_weight=100,),
                        width="80%",
                    ),
                    pc.box(
                        pc.text("INDUSTRY", font_size="3em",
                                font_weight=100,),
                        width="80%",
                    ),
                    color="white",
                    width="100%",
                    spacing="-2em",
                    font_size="1.7em",
                    _hover={
                        "opacity": 0.7,
                    },
                ),
                pc.vstack(
                    pc.box(
                        pc.hstack(
                            pc.heading("DONGYOUNG KIM, Ph.D.",
                                       font_size="3em"),
                            width="100%",
                            _hover={
                                "opacity": 0.7,
                            },
                        ),
                        width="80%",
                    ),
                    pc.box(
                        pc.hstack(
                            # pc.text("과학과 산업의 인공지능 전문가", font_weight=100,),

                            pc.avatar(src="/picture.png", size="md"),
                            pc.link(
                                pc.button(
                                    "Curriculum Vitae",

                                    background_image="white",
                                    color="#5B42F3",
                                    _hover={
                                        "opacity": 0.85,
                                    },
                                    size="lg",
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
                                    size="lg",
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
                                    size="lg",
                                ),
                                href=constants.BLOG_URL,
                                button=True,
                                is_external=True,
                            ),
                        ),
                        height="100px",
                        width="80%",
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
                                            "OCR Team Leader (General Manager) @ AI Tech", font_size="1.2em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2021 - 2021"),
                                    pc.td(
                                        pc.text("현대자동차 서울, 대한민국"),
                                        pc.text("AIRS Company"),
                                        pc.text(
                                            "Senior Manager @ MCS Lab", font_size="1.2em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2020 - 2021"),
                                    pc.td(
                                        pc.text("삼성생명 서울, 대한민국"),
                                        pc.text(
                                            "Manager @ Data Analytics Lab", font_size="1.2em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2017 - 2019"),
                                    pc.td(
                                        pc.text(
                                            "한국기초과학연구원 (IBS) 울산, 대한민국"),
                                        pc.text("첨단연성물질 연구단"),
                                        pc.text("Postdoctoral researcher",
                                                font_size="1.2em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2012 - 2016"),
                                    pc.td(
                                        pc.text(
                                            "Texas A&M University Texas, U.S.A"),
                                        pc.text("Research Assistant",
                                                font_size="1.2em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2010 - 2012"),
                                    pc.td(
                                        pc.text(
                                            "The University of Southwestern Medical Center Texas, U.S.A."),
                                        pc.text("Research Assistant",
                                                font_size="1.2em"),
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
                                            "Doctor of Philosophy in Biomedical Engineering", font_size="1.2em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2010 - 2012"),
                                    pc.td(
                                        pc.text(
                                            "The University of Texas at Dallas Texas, U.S.A."),
                                        pc.text(
                                            "Bachelor's degree in Electrical Engineering and Computer Science", font_size="1.2em"),
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
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/lvlm.png", on_click=State.right_0),
                                    pc.text("LVLM (2023)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="Large Vision-Language Model (LVLM) Training Project (2023)",
                            ),
                            projects.lvlm(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/ocr.png", on_click=State.right_1),
                                    pc.text("OCR Platform (2022)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="KB AI-OCR centrerized service platform (2022)",
                            ),
                            projects.kbaiocr(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/ocr_model.png", on_click=State.right_2),
                                    pc.text("OCR Models (2022)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="KB AI-OCR Model Training Project (2022)",
                            ),
                            projects.kbaiocrmodel(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/datalake.png", on_click=State.right_3),
                                    pc.text("Data Lake (2021)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="Hyundai Motors Data Lake Engineering Project (2021)",
                            ),
                            projects.datalake(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/sliocr.png", on_click=State.right_4),
                                    pc.text("SLI-OCR (2021)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="Samsung Life Insurance OCR project (2021)",
                            ),
                            projects.sliocr(),
                            width="100%",
                        ),
                        pc.box(padding_top="8%"),
                        pc.flex(
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(size="2xl", name="G S",
                                              on_click=State.right_5),
                                    pc.text("GraphDB (2021)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="Graph DB & Context Search Engine (2021)",
                            ),
                            projects.graphdb(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/aim.png", on_click=State.right_6),
                                    pc.text("AI Microscopy (2019)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="AI-powered transmitted light microscopy for functional analysis of live cells (2019)",
                            ),
                            projects.aim(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/hist.png", on_click=State.right_7),
                                    pc.text("AI histology (2020)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="In-silico histology staining on NIR LED array-based quantitative phase imaging (2020)",
                            ),
                            projects.hist(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/aitomography.png", on_click=State.right_8),
                                    pc.text("AI tomography (2020)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="AI assisted rapid tomography imaging modality (2020)",
                            ),
                            projects.aitomography(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/spinner.png", on_click=State.right_9),
                                    pc.text("Dx-figet (2021)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="A FIDGET SPINNER FOR THE POINT-OF-CARE DIAGNOSIS OF URINARY TRACT INFECTION (2020)",
                            ),
                            projects.spinner(),
                            width="100%",
                        ),
                        pc.box(padding_top="8%"),
                        pc.flex(
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/evident.png", on_click=State.right_10),
                                    pc.text("EV-IDENT (2020)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="EV-IDENT: IDENTIFYING TUMOR-SPECIFIC EXTRACELLULAR VESICLES BY SIZE FRACTIONATION AND SINGLE-VESICLE ANALYSIS (2020)",
                            ),
                            projects.evident(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/sr.png", on_click=State.right_11),
                                    pc.text("Super-resolution (2016)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="THREE-DIMENSIONAL SINGLE-MOLECULE LOCALIZATION SUPER-RESOLUTION MICROSCOPY (2016)",
                            ),
                            projects.sr(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/rmum.png", on_click=State.right_12),
                                    pc.text("R-MUM (2016)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="REMOTE FOCUSING MULTIFOCAL PLANE MICROSCOPY FOR THE IMAGING OF 3D SINGLE MOLECULE DYNAMICS WITH CELLULAR CONTEXT  (2016)",
                            ),
                            projects.rmum(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/her23.png", on_click=State.right_13),
                                    pc.text("HER2/HER3 (2016)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="HER2/HER3 SIGNALING OVERCOMES HEREGULIN-INDUCED RESISTANCE TO PI3K INHIBITION IN PROSTATE CANCER (2016)",
                            ),
                            projects.her23(),
                            # -------------------------------------------
                            pc.spacer(),
                            pc.tooltip(
                                pc.vstack(
                                    pc.avatar(
                                        size="2xl", src="projects/her2.png", on_click=State.right_14),
                                    pc.text("HER2 (2016)",
                                            as_="strong"),
                                    style={"cursor": "pointer"},
                                ),
                                label="THE LEVEL OF HER2 EXPRESSION IS A PREDICTOR OF ANTIBODY-HER2 TRAFFICKING BEHAVIOR IN CANCER CELLS (2016)",
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
                                            "한국지능정보시스템학회 추계 학술대회 우수논문상", font_size="1.2em"),
                                        pc.text(
                                            "Deep Learning OCR based document processing platform and its application in financial domain."),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2020"),
                                    pc.td(
                                        pc.text(
                                            "IEEE ICDAR SROIE text localization task 2020 1 위 ", font_size="1.2em"),
                                        pc.text(
                                            "https://rrc.cvc.uab.es/?ch=13&com=evaluation&task=1"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2020"),
                                    pc.td(
                                        pc.text(
                                            "IEEE ICDAR SROIE text recognition task 2020 1 위 ", font_size="1.2em"),
                                        pc.text(
                                            "https://rrc.cvc.uab.es/?ch=13&com=evaluation&task=2"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2018"),
                                    pc.td(
                                        pc.text(
                                            "Shark Tank Competition 1 위  ", font_size="1.2em"),
                                        pc.text(
                                            "The 22nd International Conference On Miniaturized Systems For Chemistry And Life Sciences, Taiwan"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2016"),
                                    pc.td(
                                        pc.text(
                                            "3D single molecule localization microscopy 부문 1 위 ", font_size="1.2em"),
                                        pc.text(
                                            "SMLMS Challenge (EPFL), Swissland"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2014 - 2016"),
                                    pc.td(
                                        pc.text(
                                            "Texas A&M University 연구 장학금, U.S.A.", font_size="1.2em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2011 - 2014"),
                                    pc.td(
                                        pc.text(
                                            "The University of Texas at Dallas 연구 장학금, U.S.A.", font_size="1.2em"),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2011"),
                                    pc.td(
                                        pc.text(
                                            "Senior Design Project 2 위 ", font_size="1.2em"),
                                        pc.text(
                                            "The University of Texas at Dallas, U.S.A."),
                                    ),
                                ),
                                pc.tr(
                                    pc.td("2010 - 2012 	"),
                                    pc.td(
                                        pc.text(
                                            "The University of Texas at Dallas 학사 장학금, U.S.A.", font_size="1.2em"),
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
                            data=pd.read_csv(constants.PATENTS_URL),
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
                width="65%",
                default_index=[0, 1, 2, 3, 4, 5, 6],
            ),

            pc.vstack(
                width="100%",
                padding_top="10%",
            ),
            width="100%",
        ),
    )
