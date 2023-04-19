import speedtest  # pip install speedtest-cli

try:
    st = speedtest.Speedtest()
except:
    print("Please check your internet connection.")


def download_speed():
    return round(st.download() / 10 ** 6, 2)


def upload_speed():
    return round(st.upload() / 10 ** 6, 2)


def ping():
    servernames = []
    st.get_servers(servernames)
    results = st.results.ping
    return results


def speed_test(*args, **kwargs):
    try:
        print("Checking internet speed. Please wait...")
        # print('Download Speed: ' + str(download_speed()) + 'MB/s')
        # print('Upload Speed: ' + str(upload_speed()) + ' MB/s')
        # print('Ping: ' + str(ping()) + ' ms')
        return (
            (
                (
                    (
                        f"Download Speed: {str(download_speed())}MB/s"
                        + "\n Upload Speed: "
                        + str(upload_speed())
                    )
                    + " MB/s"
                )
                + "\n Ping: "
            )
            + str(ping())
            + " ms"
        )
    except Exception as e:
        print(e)
        return "Error in internet speed test"


if __name__ == '__main__':
    print(speed_test())
