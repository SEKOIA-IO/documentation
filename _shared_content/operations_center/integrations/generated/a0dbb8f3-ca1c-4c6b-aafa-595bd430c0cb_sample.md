
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


=== "common_log_format_1"

    ```
	1.2.3.4 - johndoe [05/02/2025 11:30:29] "GET https://sub.example.com/1.png HTTP/1.1" 200 - - 1000 Business Services
    ```



=== "common_log_format_2"

    ```
	5.6.7.8 - janedoe [05/02/2025 11:31:06] "CONNECT https://example.com:443 HTTP/1.1" 200 -
    ```



=== "connect"

    ```
	1564655684.277   3387 192.168.0.1 TCP_TUNNEL/200 19131 CONNECT example.org:443 - HIER_DIRECT/example.org -
    ```



=== "connect2"

    ```
	1564576741.982   5756 192.168.0.1 TCP_TUNNEL/200 6295 CONNECT api42-api.example.com:443 - HIER_DIRECT/api42-api.example.com -
    ```



=== "connect3"

    ```
	1587042596.494   1717 192.168.224.39 TCP_TUNNEL/200 3512 CONNECT 193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.example.net:443 - HIER_DIRECT/193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.example.net -
    ```



=== "connect4"

    ```
	1737983758.627 207 1.2.3.4 TCP_TUNNEL/200 4047 CONNECT test.example.org:443 - HIER_DIRECT/5.6.7.8 - 
    ```



=== "connect5"

    ```
	1737983750.078 61 1.2.3.4 TCP_TUNNEL/200 8811 CONNECT safebrowsing.example.com:443 - HIER_DIRECT/5.6.7.8 -
    ```



=== "connect_ip"

    ```
	1642667037.129      0 10.0.4.4 TCP_DENIED/403 3868 CONNECT 1.2.3.4:80 - HIER_NONE/- text/html "-" "-"
    ```



=== "content_type"

    ```
	1565598801.353     24 10.16.12.86 TCP_MISS/200 394 GET http://dt.example.com/dt123456 - HIER_DIRECT/dt.example.com image/gif
    ```



=== "error"

    ```
	1761121144.919      0 1.2.3.4 NONE_NONE/000 0 - error:transaction-end-before-headers - HIER_NONE/- - "-" "-"
    ```



=== "get"

    ```
	1564670112.892   5007 192.168.95.17 TCP_HIT_ABORTED/000 0 GET http://smex10-2-en.url.example.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA== - HIER_DIRECT/smex10-2-en.url.example.com -
    ```



=== "get2"

    ```
	1565600128.411      0 192.168.0.1 TCP_DENIED/407 3980 GET http://api.example.org/api/v2/check - HIER_NONE/- text/html
    ```



=== "get_dalid"

    ```
	1628084203.491     82 192.168.2.2 TCP_MISS/200 318399 GET http://download.example.com/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab - HIER_DIRECT/1.2.3.4 application/vnd.ms-cab-compressed
    ```



=== "get_tcp_hit"

    ```
	1628150510.448    549 192.168.0.1 TCP_HIT/206 2055995 GET http://edgedl.me.example.com/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3 - HIER_NONE/- application/octet-stream
    ```



=== "get_user_agent"

    ```
	1564670112.892   5007 192.168.95.17 TCP_HIT_ABORTED/000 0 GET http://smex10-2-en.url.example.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA== - HIER_DIRECT/smex10-2-en.url.example.com - "http://www.example.org" "TMUFE"
    ```



