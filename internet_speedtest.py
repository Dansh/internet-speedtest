import speedtest
import subprocess



class InternetSpeedTest(speedtest.Speedtest):
    def __init__(self):
        super(InternetSpeedTest, self).__init__()
    
    def get_download(self):
        download = self.download()
        for _ in range(6):
            download /= 10
        download = "{:.2f}".format(download)
        return float(download)

    def get_upload(self):
        upload = self.upload()
        for _ in range(6):
            upload /= 10
        upload = "{:.2f}".format(upload)
        return float(upload)

    def get_wifi_name(self):
        strDetails = str(subprocess.check_output("netsh wlan show interfaces"))
        listDetails = strDetails.split(":")
        wifiname = listDetails[12].split("\\r")[0]
        wifiname = wifiname.replace(wifiname[0], "")
        return wifiname
    
    def get_results(self):
        download = self.get_download()
        upload = self.get_upload()
        ping = self.results.ping
        wifiname = self.get_wifi_name()
        return {'wifiname': wifiname ,'download': download, 'upload': upload, 'ping': ping}

st = InternetSpeedTest()
