# GreenEyeClient
# Prerequisite:
Have a container of the GreenEyeServer running. go to https://github.com/noamRoditi/GreenEyeServer for more details.

# Using GreenEyeClient:
  1. build the docker image using "docker build {image name} ."
  2. run "docker run -d {image name} {k} {num_samples_to_use} {num_samples_per_clusters} {server ip}".
  3. result of the request to server will be printed to screen.
