import pynecone as pc
from home.templates import webpage
from home import constants
import pandas as pd
from home.base_state import State


def lvlm():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2023 - 현재 | KB 국민은행"),
                       padding_left="1.5em", padding_top="20%"),
                pc.drawer_header(
                    "Large Vision-Language Model (LVLM) Training Project"),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(src="projects/lvlm.png",
                                 width="90%", height="auto"),
                        pc.center(pc.text("<LVLM 의 모식도 및 작동 예시>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "한글 및 영문 문서 이미지내 문자를 읽고 이해할 수 있는 Large Vision-Language Model 훈련 프로젝트 리드."),
                                pc.list_item(
                                    "Transformers Encoder-Decoder 구조로 이미지를 구획화하여 인코딩하고, 이를 한글/영문 등의 문자열로 디코딩하는 End-to-End Vision-to-Language 처리 모델."),
                                pc.list_item(
                                    "문서 읽기(OCR: Optical Character Recognition), 문서 분류(DS: Document Sorting), 정보 추출(IE: Information Extraction) 및 문서 질문 답변 (DQA: Document Question-Answering) 등의 기능을 가지는 Fine-tuning 제공."),
                                spacing="20px",
                            ),
                        ),
                        spacing="20px",
                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_0, width="95%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_0,
        size="md",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def kbaiocr():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2021 - 2022 | KB 국민은행"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "KB AI-OCR 공통플랫폼 구축 프로젝트 "),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/ocr.png", width="70%", height="auto"),
                        pc.center(
                            pc.text("<KB AI-OCR 공통 플랫폼 Hybrid GPU Cluster 및 MLOps 시스템 구성도>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "KB 국민은행내 모든 고객 및 직원 업무의 문서처리를 위한 자체개발 OCR 플랫폼 개발 리드"),
                                pc.list_item(
                                    "마이크로서비스(MSA) 문서 처리 플랫폼으로 재사용 및 확장 가능한 구조"),
                                pc.list_item(
                                    "금융 특화 Hybrid GPU Cluster 구축: on-premise kubernetes GPU cluster 및 AWS EKS 사용"),
                                pc.list_item(
                                    "MLOps 기반 문서 처리 플랫폼 개발 시스템"),
                                pc.list_item(
                                    "2022년 9월~12월간 KB국민은행 고객 및 직원을 대상으로  9가지 서비스 구축 및 운영"),
                                pc.list_item(
                                    "직원 업무 경감 서비스: 법인 고객 확인 서류 사전점검 서비스, 개인고객 확인 서류 사후 점검 서비스, 퇴직 연금 정보 입력 서비스, 외환 생션 관리 보조 서비스, 외환 거래 신청서 입력 보조 서비스, 위탁 회사 공문 처리 보조 서비스"),
                                pc.list_item(
                                    "고객 편의 서비스: 계좌 촬영 이체 서비스, 쿠폰 등록 서비스, 수험표 확인 서비스"),
                                spacing="20px",
                            ),
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),
                        pc.box(
                            pc.text(
                                "*관련 결과/수상/뉴스", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[수상] 2022 한국지능정보시스템학회 추계 학술대회 우수논문상"),
                                    pc.list_item(
                                        "[수상] 2022 대한민국 IT서비스 기술혁신 단체부문 혁신대상"),
                                    pc.list_item(
                                        "[뉴스] IT서비스 기술혁신 기업에 국민은행·CJ올리브네트웍스, 전자신문, 2022, https://www.etnews.com/20221116000100"),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[논문] Kim, D., Kim, D.-H., Kwak, M., ... Choi, D., Deep Learning OCR based document processing platform and its application in financial domain. Journal of Intelligence and Information Systems. 2023."),
                                    pc.list_item(
                                        "[특허]  김동영, 손동원, 손현수, 신예지, 김두형, 곽명성, 딥러닝 이미지 변환 기법을 통한 금융 도메인 특화 이미지 데이터 증강 시스템 (FINANCIAL DOMAIN-SPECIFIC IMAGE DATA AUGMENTATION SYSTEM THROUGH DEEP LEARNING IMAGE CONVERSION TECHNIQUE) 한국특허출원중, 2023"),
                                    pc.list_item(
                                        "[특허] 김동영, 신예지, 손현수, 김두형, 곽명성, 인공지능 금융 문서 정보 추출 시스템 (ARTIFICIAL INTELLIGENCE FINANCIAL DOCUMENT INFORMATION EXTRACTION SYSTEM) 한국특허출원중, 2023"),
                                    pc.list_item(
                                        "[특허] 김동영, 김두형, 곽명성, 딥러닝 기반 광학 문자 인식 기법을 활용한 개인 고객 확인 의무 확인 자동화 시스템 및 방법 (AUTOMATED SYSTEM AND METHOD FOR CHECKING CDD(CUSTOMER DUE DILIGENCE) USING DEEP LEARNING-BASED OPTICAL CHARACTER RECOGNITION TECHNIQUE) 한국특허출원, 10-2023-0000066, 2023"),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_1, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_1,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def kbaiocrmodel():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2021 - 2022 | KB 국민은행"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "KB AI-OCR 모델 개발 프로젝트"),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/ocr_model.png", width="60%", height="auto"),
                        pc.center(
                            pc.text("<KB AI-OCR 공통 플랫폼 Hybrid GPU Cluster 및 MLOps 시스템 구성도>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "데이터 생성모델의 데이터를 이용한 OCR 모델 개발 리드"),
                                pc.list_item(
                                    "Attention 기반의 데이터 생성모델을 통한 데이터 생성 및 이를 이용한 다양한 OCR 모델 개발"),
                                pc.list_item(
                                    "GAN을 이용한 이미지 전처리 모델, GAN을 이용한 문자 탐지 모델, STN, CNN, RNN, Attention을 이용한 문자 인식 모델, Transformer를 이용한 표 인식 및 문서 처리 모델 개발 및 적용"),
                            ),
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),
                        pc.box(
                            pc.text(
                                "*관련 결과/수상/뉴스", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[수상] 2022 한국지능정보시스템학회 추계 학술대회 우수논문상"),
                                    margin="10px",
                                    padding_left="20px",
                                    width="100%",
                                ),
                                padding="5px",
                                width="100%",
                                background_color="#F6F6F6",
                            ),
                            width="100%",
                        ),
                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[논문] Kim, D., Kim, D.-H., Kwak, M., ... Choi, D., Deep Learning OCR based document processing platform and its application in financial domain. Journal of Intelligence and Information Systems. 2023."),
                                    pc.list_item(
                                        "[특허]  김동영, 손동원, 손현수, 신예지, 김두형, 곽명성, 딥러닝 이미지 변환 기법을 통한 금융 도메인 특화 이미지 데이터 증강 시스템 (FINANCIAL DOMAIN-SPECIFIC IMAGE DATA AUGMENTATION SYSTEM THROUGH DEEP LEARNING IMAGE CONVERSION TECHNIQUE) 한국특허출원중, 2023"),
                                    pc.list_item(
                                        "[특허] 김동영, 신예지, 손현수, 김두형, 곽명성, 인공지능 금융 문서 정보 추출 시스템 (ARTIFICIAL INTELLIGENCE FINANCIAL DOCUMENT INFORMATION EXTRACTION SYSTEM) 한국특허출원중, 2023"),
                                    pc.list_item(
                                        "[특허] 김동영, 김두형, 곽명성, 딥러닝 기반 광학 문자 인식 기법을 활용한 개인 고객 확인 의무 확인 자동화 시스템 및 방법 (AUTOMATED SYSTEM AND METHOD FOR CHECKING CDD(CUSTOMER DUE DILIGENCE) USING DEEP LEARNING-BASED OPTICAL CHARACTER RECOGNITION TECHNIQUE) 한국특허출원, 10-2023-0000066, 2023"),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_2, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_2,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def datalake():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2021 - 2021 | 현대자동차"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "셔클 서비스 DataLake 구축 프로젝트"),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/datalake.png", width="85%", height="auto"),
                        pc.center(
                            pc.text("<셔클 서비스 DataLake내 데이터 처리 파이프라인>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "현대자동차에서 서비스하는 셔클 서비스에서 실시간으로 생성되는 데이터를 저장, 정제하여 비지니스 인텔리전스(BI) 및 서비스 리포팅에 필요한 API로 데이터를 제공할 수 있는 DataLake 구축 리드"),
                                pc.list_item(
                                    "마이크로서비스 컨테이너내 gRPC 로 통신되는 모든 데이터를 Kafka 및 Kafka stream 을 통해 수집하고, 이를 Amazon EMR(Apache Spark)을 이용해 Delta Lake 에 수집, 처리, 정제하여 저장"),
                                pc.list_item(
                                    "Delta Lake 의 데이터는 Hive 구조화하고, 이를 Amazon Athena 를 통해 rehash 와 같은 BI Tool 에서 호출할수 있도록 함. Redash 는 데이터 시각화 "),
                                pc.list_item(
                                    "도출된 자료는 필요에 따라 자동화된 API 루틴을 통해 보안 공개되며, 이는 Amazon Lambda 및 API G/W 를 통해 데이터 서비스로서 제공할수 있는 파이프라인 구성"),
                                spacing="20px",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_3, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_3,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def sliocr():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2020 - 2021 | 삼성생명"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "SLI-OCR 모델 개발 프로젝트"),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/sliocr.png", width="60%", height="auto"),
                        pc.center(
                            pc.text("<서류 지옥서 구해준 ‘딥러닝 OCR’에 세계가 ‘엄지 척’ , 조선일보 2010. 10. 29>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "인공지능 기술을 이용한 OCR 및 데이터 구조화 모델 개발 프로젝트 리드"),
                                pc.list_item(
                                    "데이터 생성 시뮬레이터, 이미지 전처리, 문자 탐지, 문자 인식, 데이터 구조화 모델 설계 및 훈련"),
                                pc.list_item(
                                    "Redis/Celery 를 이용한 OCR 서비스 프로그램 구현"),
                                spacing="20px",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),
                        pc.box(
                            pc.text(
                                "*관련 결과/수상/뉴스", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[뉴스] 조선일보 2010. 10. 29. 서류 지옥서 구해준 ‘딥러닝 OCR’에 세계가 ‘엄지 척’ "),
                                    pc.list_item(
                                        "[수상] ICDAR SROIE leaderboard text localization 1st place (2020/12)"),
                                    pc.list_item(
                                        "[수상] ICDAR SROIE leaderboard text recognition 1st place (2020/12)"),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",
                                background_color="#F6F6F6",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        pc.image(
                            src="projects/sliocr2.png", width="70%", height="auto"),
                        pc.center(
                            pc.text("<ICDAR SROIE leaderboard text localization & recognition 1위, 2020/12>")),
                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[논문] Kim, D., Kwak, M., Won, E., Shin, S., & Nam, J. TLGAN: document Text Localization using Generative Adversarial Nets. Arxiv 2010.1154, 2020."),
                                    pc.list_item(
                                        "[특허] 김동영, 곽명성, 원은지, 신세정, 인공지능 기반 광학 이미지 데이터 고품질화 방법 (METHOD FOR MAKING HIGH QUALITY OF OPTICAL IMAGE DATA BASED ON ARTIFICIAL INTELLIGENCE) 한국특허등록 1024182080000, 2022. "),
                                    pc.list_item(
                                        "[특허] 김동영, 곽명성, 원은지, 광학이미지문서 생성을 위한 인공지능 기반 시뮬레이터 (METHOD FOR MANAGING TRAINING DATA FOR OPTICAL CHARACTER RECOGNITION), 한국특허등록 1024861050000, 2022. "),
                                    pc.list_item(
                                        "[특허] 김동영, 곽명성, 남정연, 인공지능 기반 비정형 데이터 해석방법 (METHOD FOR INTERPRETATING UNSTRUCTURED DATA BASED ON ARTIFICIAL INTELLIGENCE), 한국특허등록 1024576500000, 2022. "),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_4, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_4,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def graphdb():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2020 - 2021 | 삼성생명"),
                       padding_left="1.5em", padding_top="50%"),
                pc.drawer_header(
                    "금융 지식 그래프 / 기계 독해 검색 엔진 개발"),

                pc.drawer_body(
                    pc.vstack(
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "사내 금융 지식 (KMS) 및 상품정보의 인공지능 분석 기술 개발 리드"),
                                pc.list_item(
                                    "SLI-BERT pretrained model 훈련"),
                                pc.list_item(
                                    "사내 금융 지식 및 상품정보 벡터화를 통한 context search engine 개발 "),
                                pc.list_item(
                                    "Context serach engine 을 활용한 RDB to GraphDB (Neo4J) 방법론 개발 및 GraphDB 구축"),
                                pc.list_item(
                                    "SLI-miniGPT 엔진 개발 및 topic specific text generation engine 구축"),
                                spacing="20px",
                            ),
                        ),

                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_5, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_5,
        size="md",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def aim():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2017 - 2019 | 한국기초과학연구원"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "인공지능현미경 (AI-powered transmitted light microscopy for functional analysis of live cells)"),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/aim.png", width="90%", height="auto"),
                        pc.center(
                            pc.text("<인공지능 현미경 시스템 구조 및 동작 예시>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "Unsupervised machine learning 과 supervised semantic segmentation 을 이용한 transmitted light microscopy image 를 fluorescence microscopy image 로 바꾸는 기술 개발"),
                                pc.list_item(
                                    "Region proposal convolutional neural network 및 convolutional neural network 를 이용한 transmitted light microscopy image 내의 세포 상태 실시간 모니터링."),
                                pc.list_item(
                                    "Time-lapse 영상 내의 세포를 complementary learner 를 이용한 tracking 및 모니터링."),
                                spacing="20px",
                            ),
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),
                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[논문] Kim, D., Min, Y., Oh, J.M. et al. AI-powered transmitted light microscopy for functional analysis of live cells. Sci Rep 9, 18428 (2019) doi:10.1038/s41598-019-54961-x "),
                                    pc.list_item(
                                        "[특허] 김동영, 민유홍, 조윤경, 인공신경망을 이용한 세포 영상 분석 방법 및 세포 영상 처리 장치 (ANALYSING METHOD FOR CELL IMAGE USING ARTIFICIAL NEURAL NETWORK AND IMAGE PROCESSING APPARATUS FOR CELL IMAGE). 한국특허등록 1020846830000, 2020."),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_6, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_6,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def hist():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2019 - 2020 | 한국기초과학연구원"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "인공지능 조직학 이미지 촬영 기술 (In-silico histology staining on NIR LED array-based quantitative phase imaging)"),
                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/hist.png", width="90%", height="auto"),
                        pc.center(
                            pc.text("<인공지능 조직학 이미징 시스템 구조 및 동작 예시>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "Near-Infrared LED array 를 이용한 absorption-free quantitative phase imaging 기술 개발"),
                                pc.list_item(
                                    "Stained histology slides 의 NIR quantitative phase imaging 및 Transmitted light imaging 을 통한 registration-free single-shot training data acquisition."),
                                pc.list_item(
                                    "Generative adversarial networks (GAN) 을 이용한 phase image to histology image translation model training"),
                                pc.list_item(
                                    "Brain 및 Kidney 에 대해 모델 훈련 및 결과물에 대해 20명의 병리연구사의 Mean Opinion Score 평가에 있어 유의미한 차이 없음 확인"),
                                spacing="20px",
                            ),
                        ),
                        spacing="20px",
                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_7, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_7,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def aitomography():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2019 - 2020 | 한국기초과학연구원"),
                       padding_left="1.5em", padding_top="30%"),
                pc.drawer_header(
                    "인공지능 초고속 3차원 단층촬영 기법 (AI assisted rapid tomography imaging modality)"),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/aitomography.png", width="95%", height="auto"),
                        pc.center(
                            pc.text("<인공지능 초고속 단층촬영>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "의료용 단층촬영 수행에 있어 여러장의 2차원 슬라이스 단층 이미지를 획득하고, 이로부터 부터 3차원 볼륨을 재구성 하는 작업을 수행함에 있어 적은수의 2차원 슬라이스 단층 이미지로 부터 고해상도 3차원 볼륨을 복원하는 인공지능 기법 개발"),
                                pc.list_item(
                                    "촬영 시간 단축을 통해 피사체의 움직임을 최소화 함으로 고품질의 3차원 볼륨을 얻을 수 있음"),
                                spacing="20px",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_8, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_8,
        size="md",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def spinner():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2017 - 2020 | 한국기초과학연구원"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "A FIDGET SPINNER FOR THE POINT-OF-CARE DIAGNOSIS OF URINARY TRACT INFECTION"),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/spinner.png", width="70%", height="auto"),
                        pc.center(
                            pc.text("<요로 감염 검사를 위한 피잿 스피너 구조 및 작동 원리>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "Bacterial cell enrichment 를 위한 Hand-powered microfluidic system 개발"),
                                pc.list_item(
                                    "Urine 내의 bacterial 함량 측정 및 drug resistance test 를 통한 Extreme Point-Of-Care-Testing 실현"),
                                pc.list_item(
                                    "Enriched bacterial cell의 정량화를 위한 computer vision 도구 및 모델 개발"),
                                spacing="20px",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),
                        pc.box(
                            pc.text(
                                "*관련 결과/수상/뉴스", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[수상] 대만 The 22nd International Conference On Miniaturized Systems For Chemistry And Life Sciences, Shark Tank Competition 1 위 (2018)"),
                                    pc.list_item(
                                        "[뉴스] MBC 뉴스 “장난감 원리로 감연진단… 피젯 스피너의 변신” (2020)"),
                                    pc.list_item(
                                        "[뉴스] NewScientist 뉴스 “Fidget spinner device can diagnose UTIs in under an hour without a lab” (2020)"),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[논문] Kim, D., Michael, I., Gulenko, O., Kumar, S., Kumar, S., Clara, J., … Cho, Y.-K. (2020). A fidget spinner for the point-of-care diagnosis of urinary tract infection. Nature Biomedical Engineering. https://doi.org/10.1038/s41551-020-0557-2."),
                                    pc.list_item(
                                        "[특허] 김동영, 미카엘 아이작, 기동엽, 조윤경, 원심력 기반 무전원 입자 농축장치 및 입자 농축방법(Centrifugal force based non-powered particle concentration apparatus and method of particle concentration). 한국특허1021037840000, 2020. "),
                                    pc.list_item(
                                        "[특허] 김동영, 김치주, 기동엽, 조윤경, 원심력 기반 혈소판 분리 및 검진 장치(Centrifugal force based platelet isolation and testing system). 한국특허1020638650000, 2020."),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_9, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_9,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def evident():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2017 - 2020 | 한국기초과학연구원"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "EV-IDENT: IDENTIFYING TUMOR-SPECIFIC EXTRACELLULAR VESICLES BY SIZE FRACTIONATION AND SINGLE-VESICLE ANALYSIS"),
                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/evident.png", width="90%", height="auto"),
                        pc.center(
                            pc.text("<EV-IDENT의 작동 구조 및 분석 방법>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "혈액내 나노소포체 분석 및 기계학습을 통한 암 조기 진단 기술 개발"),
                                pc.list_item(
                                    "Particle optical image modeling / localization optimization 을 통한 정량화 및 single photon count 를 통한 정확한 protein marker expression 측정"),
                                pc.list_item(
                                    "Unsupervised / supervised machine learning 을 이용한 혈액 내 체내 건강정보 및 암 세포 조기 검출 수행"),
                                spacing="20px",
                            ),
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),
                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[논문] Kim, D., Woo, H.-K., Lee, C., Min, Y., Kumar, S., Sunkara, V., … Cho, Y.-K. (2020). EV-Ident: Identifying Tumor-Specific Extracellular Vesicles by Size Fractionation and Single-Vesicle Analysis. Analytical Chemistry, 92(8), 6010–6018. https://doi.org/10.1021/acs.analchem.0c00285"),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_10, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_10,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def sr():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2012 - 2016 | Texas A&M University"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "THREE-DIMENSIONAL SINGLE-MOLECULE LOCALIZATION SUPER-RESOLUTION MICROSCOPY"),
                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/sr.png", width="90%", height="auto"),
                        pc.center(
                            pc.text("<SINGLE-MOLECULE LOCALIZATION SUPER-RESOLUTION MICROSCOPY 예시>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "광학현미경을 이용하여 광학한계인 250nm 해상도의 100배인 2.5 nm 초고해상도의영상을 얻어내는 기술 개발"),
                                pc.list_item(
                                    "Photon modeling 및 localization (MLE, EM) 을 통한 이미지 내 광자의 위치 추적."),
                                pc.list_item(
                                    "다초점 기술 (multifocal plane microscopy) 의 적용으로 3차원 구현"),
                                spacing="20px",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),
                        pc.box(
                            pc.text(
                                "*관련 결과/수상/뉴스", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[수상] 스위스 SMLMS Challenge (EPFL) 3D single molecule localization microscopy 부문 1 위 "),
                                    margin="10px",
                                    padding_left="20px",
                                    width="100%",
                                ),
                                padding="5px",
                                width="100%",
                                background_color="#F6F6F6",
                            ),
                            width="100%",
                        ),
                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[논문] Cohen E. A. K.,. Kim D., Ober R.J, Cramer-Rao Lower Bound for Point Based Image Registration with Heteroscedastic Error Model for Application in Single Molecule Microscopy. IEEE Transactions on Medical Imaging 2015"),
                                    pc.list_item(
                                        "[논문] Ram S, Kim D, Ober RJ, Ward ES. 3D Single Molecule Tracking with Multifocal Plane Microscopy Reveals Rapid Intercellular Transferrin Transport at Epithelial Cell Barriers. Biophysical Journal 2012"),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_11, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_11,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def rmum():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2014 - 2016 | Texas A&M University"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "REMOTE FOCUSING MULTIFOCAL PLANE MICROSCOPY FOR THE IMAGING OF 3D SINGLE MOLECULE DYNAMICS WITH CELLULAR CONTEXT"),
                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/rmum.png", width="90%", height="auto"),
                        pc.center(
                            pc.text("<REMOTE FOCUSING MULTIFOCAL PLANE MICROSCOPY 구조>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "세포 내 분자의 움직임과 그 주변환경을 3차원 영상으로 보여주는 기술 개발"),
                                pc.list_item(
                                    "영상으로부터 분자의 3차원 위치를 10nm 정확도로 초정밀 추정"),
                                pc.list_item(
                                    "주변환경의 3차원 영상을 광학 허상으로부터 기록"),
                                pc.list_item(
                                    "여러 카메라 및 센서로 부터 기록된 다차원 영상데이터의 시공간의 초정밀 합성 (Spatial-temporal registration)"),
                                spacing="20px",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),
                        pc.box(
                            pc.text(
                                "*관련 결과/수상/뉴스", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[수상] 스위스 SMLMS Challenge (EPFL) 3D single molecule localization microscopy 부문 1 위 "),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",
                                width="100%",
                                background_color="#F6F6F6",
                            ),
                            width="100%",
                        ),
                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[특허] Kim D., Ober R.J, Advanced multi-dimensional microscopy system for single particle & structure imaging. U.S. Patent, 2017"),
                                    pc.list_item(
                                        "[논문] Kim, D., Chao, J., Velmurugan, R., You, S., Ward, E. S., and Ober, R. J. Remote focusing multifocal plane microscopy for the imaging of 3D single molecule dynamics with cellular context. Proceedings of the SPIE, Three-Dimensional and Multidimensional Microscopy: Image Acquisition and Processing XXIV, 10070: 2017"),
                                    pc.list_item(
                                        "[논문] Kim D, You S, Ward E.S., Ober R.J, Imaging of three-dimensional single molecule dynamics with cellular context: Antibody trafficking and interaction with cell membrane and sorting endosomes. ASCB, San Fransisco, CA. 2016"),
                                    pc.list_item(
                                        "[논문] Cohen E. A. K.,. Kim D., Ober R.J, Cramer-Rao Lower Bound for Point Based Image Registration with Heteroscedastic Error Model for Application in Single Molecule Microscopy. IEEE Transactions on Medical Imaging 2015"),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_12, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_12,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def her23():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2014 - 2016 | Texas A&M University"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "HER2/HER3 SIGNALING OVERCOMES HEREGULIN-INDUCED RESISTANCE TO PI3K INHIBITION IN PROSTATE CANCER"),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/her23.png", width="95%", height="auto"),
                        pc.center(
                            pc.text("<HER2-HER3 Engineered Antibody 와 그에 따른 암세포에서의 PI3K 신호 변화 및 intracellular trafficking>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "HER2 및 HER3 를 동시에 targeting 하는 HER2-HER3 Engineered Antibody 개발 및 특성 연구"),
                                pc.list_item(
                                    "HER2/HER3 co-binding 시 prostate cancer 에서 PI3K 억제에 효과 있음을 입증"),
                                spacing="20px",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),

                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[논문] Poovasery J.S., Kang J.C., Kim D., Ober R.J, Ward E.S. Antibody targeting of HER2/HER3 signaling overcomes heregulin-induced resistance to PI3K inhibition in prostate cancer. International Journal of Cancer 2017"),
                                    pc.list_item(
                                        "[논문] Li, R., Chiguru, S., Li, L., Kim, D., Velmurugan, R., Kim, D., Tian, H., Schroit, A., Mason, R., Ober, R. J. and Ward, E. S. Targeting phosphatidylserine with calcium-dependent protein-drug conjugates for the treatment of cancer. Molecular Cancer Therapeutics, 2018."),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_13, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_13,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )


def her2():
    return pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.box(pc.text("2013 - 2016 | Texas A&M University"),
                       padding_left="1.5em", padding_top="5%"),
                pc.drawer_header(
                    "THE LEVEL OF HER2 EXPRESSION IS A PREDICTOR OF ANTIBODY-HER2 TRAFFICKING BEHAVIOR IN CANCER CELLS"),

                pc.drawer_body(
                    pc.vstack(
                        pc.image(
                            src="projects/her2.png", width="95%", height="auto"),
                        pc.center(
                            pc.text("<HER2 expression 에 따른 cellular trafficking 변화 및 형광현미경 증적>")),
                        pc.box(
                            pc.unordered_list(
                                pc.list_item(
                                    "세포 표면의 HER2 생성량에 따라 HER2 의 intracellular trafficking 이 상이함을 밝힘"),
                                pc.list_item(
                                    "Fluorescence quenching 을 이용한 세포 내외부 단백질 발현 및 그 위치에 대한 정량화"),
                                spacing="20px",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        pc.divider(
                            variant="dashed", border_color="black"),
                        pc.box(
                            pc.text(
                                "*관련 논문/특허", as_="strong"),
                            pc.box(
                                pc.unordered_list(
                                    pc.list_item(
                                        "[논문] Ram S, Kim D, Ober RJ, Ward ES. The level of HER2 expression is a predictor of antibody- HER2 trafficking behavior in cancer cells. mAbs 2014 "),
                                    pc.list_item(
                                        "[논문] Devanaboyina SC, Lynch SM, Ober RJ, Ram S, Kim D, Puig-Canto A, Breen S, Kasturirangan S, Fowler S, Peng L, et al. The effect of pH dependence of antibody-antigen interactions on subcellular trafficking dynamics. mAbs 2013"),
                                    margin="10px",
                                    padding_left="20px",
                                ),
                                padding="5px",

                                background_color="#F6F6F6",
                            ),
                        ),
                        spacing="20px",

                    ),
                ),
                pc.drawer_footer(
                    pc.center(
                        pc.button(
                            "Close", on_click=State.right_14, width="950%",
                        ),
                        width="100%",
                    ),
                ),
            ),
        ),
        is_open=State.show_right_14,
        size="xl",
        close_on_overlay_click=True,
        close_on_esc=True,
    )
