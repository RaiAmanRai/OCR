FROM pytorch/pytorch

# if you forked EasyOCR, you can pass in your own GitHub username to use your fork
# i.e. gh_username=myname
ARG gh_username=RaiAmanRai
ARG service_home="/home/OCR"

# Configure apt and install packages
RUN apt-get update -y && \
    apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-dev \
    git \
    # cleanup
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists

# Clone EasyOCR repo
RUN mkdir "$service_home" \
    && git clone "https://github.com/$gh_username/OCR.git" "$service_home" \
    && cd "$service_home" \
    && git remote add upstream "https://github.com/RaiAmanRai/OCR.git" \
    && git pull upstream master

RUN git clone --recursive -b jax-jp4.6.1-trt7 https://github.com/akamboj2/torch2trt.git torch2trt && \
    cd torch2trt && \
    sudo python3 setup.py install --plugins

# Build
RUN cd "$service_home" \
    && python setup.py build_ext --inplace -j 4 \
    && python -m pip install -e .
