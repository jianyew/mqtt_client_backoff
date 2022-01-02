1. c demo

$ cd 
$ mkdir build && cd build
$ cmake .. \
-DBROKER_ENDPOINT="http://a3k9okwzah2uac-ats.iot.ap-northeast-1.amazonaws.com" \
-DAWS_IOT_ENDPOINT="http://a3k9okwzah2uac-ats.iot.ap-northeast-1.amazonaws.com" \
-DROOT_CA_CERT_PATH="./AmazonRootCA1.pem" \
-DCLIENT_CERT_PATH="./fa0a2a12d543819bb5f2c5d79313a54188b3409f937ad1977b4b4ae9ff0e57cc-certificate.pem.crt" \
-DCLIENT_PRIVATE_KEY_PATH="./fa0a2a12d543819bb5f2c5d79313a54188b3409f937ad1977b4b4ae9ff0e57cc-private.pem.
# AWS_IOT_ENDPOINT
$ make mqtt_demo_mutual_auth
./bin/mqtt_demo_basic_tls





client demo code

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