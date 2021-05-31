import sys
import json
import requests


class KmeanClient:

    def __init__(self, k, num_samples_to_use, num_samples_per_clusters, ip):

        self.k = k
        self.num_samples_to_use = num_samples_to_use
        self.num_samples_per_clusters = num_samples_per_clusters
        self.ip = ip
        print(f'Got k={k}, num_samples_to_use={num_samples_to_use}, num_samples_per_clusters={num_samples_per_clusters}')

    def run(self):
            result = self.send_request()
            if not self.validate_result(result):
                return
            self.save_result(result)

    def send_request(self):
        print('Sending request...')
        try:
            print(f"Going to request http://{self.ip}:5000/?k={self.k}&num_samples_to_use={self.num_samples_to_use}&num_samples_per_clusters={self.num_samples_per_clusters}")
            result = requests.get(f"http://{self.ip}:5000/?k={self.k}&num_samples_to_use={self.num_samples_to_use}"
                              f"&num_samples_per_clusters={self.num_samples_per_clusters}").text
            print('Done sending request')
            return result
        except:
            print('Failed to send request')
            exit(-1)



    def validate_result(self, result):
        try:
            self.result = json.loads(result)
            if self.result['status'] != 'success':
                print(f"Failed to get correct response! reason is {result['reason']}")
                return False
            return True
        except:
            print(f"Failed to get correct response! response is {result}")
            return False

    def save_result(self, result):
        print(result)


def validate_arguments():
    if len(sys.argv[1:]) != 4:
        print('Please provide k, num_samples_to_use and num_samples_per_clusters, server ip.')
        return False
    for arg in sys.argv[1:3]:
        if not is_valid_integer_input(arg):
            return False
    return True


def is_valid_integer_input(value):
    try:
        val = int(value)
        return True
    except ValueError:
        print("Input can only be integer please run again..")
        return False


if __name__ == '__main__':
    print('Client running')
    if not validate_arguments():
        sys.exit("Didn't receive valid arguments!")
    client = KmeanClient(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    client.run()
    print('Done')
