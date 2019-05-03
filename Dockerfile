FROM nginx:stable

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    python-pip \
    python2.7 \
    python2.7-dev \
    ssh \
    libcairo2-dev \
    python-dev \
    python-cairo-dev \
    python-imaging \
    libcairo2-dev \
    liblcms2-dev \
    libpango1.0-dev \
    graphicsmagick \
    python-wand \
    python-reportlab \
    libmagickwand-dev \
    sudo \
    && apt-get autoremove \
    && apt-get clean

RUN pip install pycairo
RUN pip install magickwand
RUN pip install pillow

ADD uniconvertor-2.0rc4 /usr/share/uniconvertor
WORKDIR /usr/share/uniconvertor
RUN python setup-uc2.py build && python setup-uc2.py bdist_deb && dpkg -i dist/python-uniconvertor-2.0rc4_amd64.deb && uniconvertor

ENTRYPOINT cd /usr/share/uniconvertor && uniconvertor /opt/cleverbrush_files/thumbnails/ma4tan7p6rfdvfmjhw_0/ma4tan7p6rfdvfmjhw_0.svg /opt/cleverbrush_files/input.pdf 
