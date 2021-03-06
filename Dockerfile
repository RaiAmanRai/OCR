FROM nvcr.io/nvidia/pytorch:22.06-py3

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

# RUN git clone https://github.com/NVIDIA-AI-IOT/torch2trt torch2trt && \
#     cd torch2trt && \
#     python3 setup.py install

# Build
RUN cd "$service_home" \
    && python setup.py build_ext --inplace -j 4 \
    && python -m pip install -e .
