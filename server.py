from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<html>
<head>
<title>List of Protocols in TCP/IP Protocol Suite</title>
</head>
<body>
    
    <table align='center' border='1'>
        <caption>List of Protocols in TCP/IP Protocol Suite</caption>
            <tr><th>S.No</th><th>Name of the Layer</th><th>Name of the Protocol</th></tr>
            <tr><td>1.</td><td>Application Layer</td><td>HTTP,FTP,DNS,SSH</td></tr>
            <tr><td>2.</td><td>Transport Layer</td><td>TCP,UDP</td></tr>
            <tr><td>3.</td><td>Internet Layer</td><td>ICMP,IGMP,ARP,IPv4/IPv6</td></tr>
            <tr><td>4.</td><td>Network Access Layer</td><td>MAC/Ethernet,FDDI,Frame Relay</td></tr>
    </table>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()