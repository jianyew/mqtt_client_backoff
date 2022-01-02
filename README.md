


#Algorithm

指数回退算法以指数方式重试请求，将重试之间的等待时间增加到最大回退时间。例如:
向服务提出请求。
1. 如果请求失败，请等待1 + random_number_milliseconds秒后重试请求。
2. 如果请求失败，等待2 + random_number_milliseconds秒，然后重试请求。
3. 如果请求失败，请等待4 + random_number_milliseconds秒后重试请求。

以此类推，直到最大回退时间。
继续等待和重试，直到重试次数达到某个最大值，但不要增加两次重试之间的等待时间。
等待时间为min (((2^n) + random_number_milliseconds, maximum_backoff)，每次迭代(或请求)n增加1。

Random_number_milliseconds有助于避免在某些情况下，许多客户端被同步，所有的重试，以同步波发送请求。
random_number_milliseconds的值在每次重试请求后重新计算。
Maximum_backoff通常是32或64秒。
适当的值取决于用例。
客户端可以在达到最大回退时间后继续重试。
在此点后重试不需要继续增加回退时间。
例如，假设客户机使用64秒的maximum_backoff时间。
达到这个值后，客户端可以每64秒重试一次。
在某些情况下，应该阻止客户无限期地重试。
重试之间的等待时间和退休数量取决于您的用例和网络条件。




##  demo for c

$ cd 

$ mkdir build && cd build

$ cmake .. \
-DBROKER_ENDPOINT="http://a3k9okwzah2uac-ats.iot.ap-northeast-1.amazonaws.com" \
-DAWS_IOT_ENDPOINT="http://a3k9okwzah2uac-ats.iot.ap-northeast-1.amazonaws.com" \
-DROOT_CA_CERT_PATH="./AmazonRootCA1.pem" \
-DCLIENT_CERT_PATH="./fa0a2a12d543819bb5f2c5d79313a54188b3409f937ad1977b4b4ae9ff0e57cc-certificate.pem.crt" \
-DCLIENT_PRIVATE_KEY_PATH="./fa0a2a12d543819bb5f2c5d79313a54188b3409f937ad1977b4b4ae9ff0e57cc-private.pem

AWS_IOT_ENDPOINT
$ make mqtt_demo_mutual_auth
./bin/mqtt_demo_basic_tls

### client demo code
```
IF bSetParameter THEN
  bSetParameter := FALSE;
  fbMqttClient.stTLS.sCA := '..\Certificates\root.pem';
  fbMqttClient.stTLS.sCert := '..\Certificates\7613eee18a-certificate.pem.crt';
  fbMqttClient.stTLS.sKeyFile := '..\Config\Certificates\7613eee18a-private.pem.key';
  fbMqttClient.sHostName:= 'a35raby201xp77.iot.eu-west-1.amazonaws.com';
  fbMqttClient.nHostPort:= 8883;
  fbMqttClient.sClientId:= 'CX-12345';
  fbMqttClient.ipMessageQueue := fbMessageQueue;
  fbMqttClient.ActivateExponentialBackoff(T#1S, T#30S);
END_IF
```

## Demo for python
具体看 py_demo:

1. import retry.py
2. demo code 
```python
@retry(wait_random_min=1000, wait_random_max=2000)
def send(i):
  #Declaring our variables
    message ={
      'thing': "device01",
      'no': i,
      'ct': time.asctime(time.localtime(time.time()) ),
      'message': "Test Message"
    }

    #Encoding into JSON
    message = mqttc.json_encode(message)
```






