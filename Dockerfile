FROM python:2.7

# Remove system buffers for stdin/stdout/stderr although it doesn't matter much
ENV PYTHONUNBUFFERED 1

# Copy packages list
COPY ./requirements.txt /requirements.txt

# Install packages, create system group, user
RUN pip install -r /requirements.txt \
    && groupadd -r scan \
    && useradd -r -g scan scan

# Copy our application code to /app
COPY . /app

# Change permissions
RUN chown -R scan /app

# Copy starter script
COPY ./entrypoint.sh /entrypoint.sh

# Change permissions of the script file
RUN sed -i 's/\r//' /entrypoint.sh \
    && chmod +x /entrypoint.sh \
    && chown scan /entrypoint.sh

# Switch to application directory
WORKDIR /app

# Open port 5000
EXPOSE 5000

# Start execution of the starter script
ENTRYPOINT ["/entrypoint.sh"]
