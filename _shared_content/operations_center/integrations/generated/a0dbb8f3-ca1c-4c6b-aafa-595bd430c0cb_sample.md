
### Raw Events Samples

In this section, you will find examples of raw logs as generated natively by the source. These examples are provided to help integrators understand the data format before ingestion into Sekoia.io. It is crucial for setting up the correct parsing stages and ensuring that all relevant information is captured.


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
	1587042596.494   1717 192.168.224.39 TCP_TUNNEL/200 3512 CONNECT 193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.akamaihd.net:443 - HIER_DIRECT/193-164-229-102_s-2-18-244-11_ts-1587042594-clienttons-s.akamaihd.net -
    ```



=== "connect4"

    ```
	1737983758.627 207 1.2.3.4 TCP_TUNNEL/200 4047 CONNECT test.domain.org:443 - HIER_DIRECT/5.6.7.8 - 
    ```



=== "connect5"

    ```
	1737983750.078 61 1.2.3.4 TCP_TUNNEL/200 8811 CONNECT safebrowsing.googleapis.com:443 - HIER_DIRECT/5.6.7.8 -
    ```



=== "connect_ip"

    ```
	1642667037.129      0 10.0.4.4 TCP_DENIED/403 3868 CONNECT 45.138.98.34:80 - HIER_NONE/- text/html "-" "-"
    ```



=== "content_type"

    ```
	1565598801.353     24 10.16.12.86 TCP_MISS/200 394 GET http://dt.adsafeprotected.com/dt?anId=929475&asId=f0fc9c04-7168-68e3-32ca-6cc17dd2223a&tv={c:l4fyeI,pingTime:-1,time:7884,type:u,clog:[{piv:100,vs:i,r:,w:1,h:1,t:78},{piv:0,vs:o,r:l,t:5971}],ndt:6,es:0,sc:1,ha:1,gm:1,slTimes:{i:5971,o:1913,n:0,pp:0,pm:0},slEvents:[{sl:i,t:78,wc:0.0.1920.1040,ac:952.74.1.1,am:i,cc:952.74.1.1,piv:100,obst:0,th:0,reas:,bkn:{piv:[5898~100],as:[5898~1.1]}},{sl:o,t:5971,wc:0.0.1920.1040,ac:952.-516.1.1,am:i,cc:952.-516.1.1,piv:0,obst:0,th:0,reas:l,bkn:{piv:[1914~0],as:[1914~1.1]}}],slEventCount:2,em:true,fr:true,e:,tt:jload,dtt:254,metricIdList:[publ1,grpm1],fm:ryV6ZcU+11|12|13|14*.929475|141|15.929475|151|152|16,idMap:14.c4c75fac-ccbe-9ba7-61b1-d1276709f9ec.31_289523-36779676|14*,rend:0,renddet:WINDOW,rmeas:0,lt:1}&br=c - HIER_DIRECT/dt.adsafeprotected.com image/gif
    ```



=== "get"

    ```
	1564670112.892   5007 192.168.95.17 TCP_HIT_ABORTED/000 0 GET http://smex10-2-en.url.trendmicro.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA== - HIER_DIRECT/smex10-2-en.url.trendmicro.com -
    ```



=== "get2"

    ```
	1565600128.411      0 192.168.0.1 TCP_DENIED/407 3980 GET http://api.example.org/api/v2/check - HIER_NONE/- text/html
    ```



=== "get_dalid"

    ```
	1628084203.491     82 192.168.2.2 TCP_MISS/200 318399 GET http://download.windowsupdate.com/c/msdownload/update/others/2019/07/29477140_324519a81d0af914f765c56a1dc7141a5759ad4c.cab - HIER_DIRECT/13.107.4.50 application/vnd.ms-cab-compressed
    ```



=== "get_tcp_hit"

    ```
	1628150510.448    549 192.168.0.1 TCP_HIT/206 2055995 GET http://edgedl.me.gvt1.com/edgedl/release2/chrome_component/adbzvrjxj3ir3yvy5lknhgbxo6tq_92.267.200/gkmgaooipdjhmangpemjhigmamcehddo_92.267.200_win64_ac37t7snjqk4qthomil6kwgo54hq.crx3 - HIER_NONE/- application/octet-stream
    ```



=== "get_user_agent"

    ```
	1564670112.892   5007 192.168.95.17 TCP_HIT_ABORTED/000 0 GET http://smex10-2-en.url.trendmicro.com/T/152/oiCEKI6Xe7maaxpSHK-gvDyUEBfC6_avSkwxG5MiT4-LQlujnVUK3SbBFHZKimvaG-TwxeMEqOnp0BelYbpVeMfVAZU85B8kltUSjYiidio-IBs_8MdCCFayLkMpM2lboKcOX-RrnDx2oFrUco0cMA== - HIER_DIRECT/smex10-2-en.url.trendmicro.com - "http://www.example.org" "TMUFE"
    ```



