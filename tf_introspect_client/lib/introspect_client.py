import requests
import xmltodict

from tf_introspect_client.lib.introspect_data import IntrospectData, NodeStatus


class IntrospectClient:
    def __init__(self, ip, port, protocol='http'):
        self.ip = ip
        self.port = port
        self.protocol = protocol

    @property
    def url(self):
        return "{proto}://{ip}:{port}".format(
            proto=self.protocol, ip=self.ip, port=self.port)

    def send_get(self, uri):
        response = requests.get("{url}/{uri}".format(url=self.url,
                                                     uri=uri))
        response.raise_for_status()
        return response

    def Snh_SandeshUVECacheReq(self, tname='', key=''):
        uri = "Snh_SandeshUVECacheReq?tname="+tname+"&key="+key
        response = self.send_get(uri)

        xmldata = response.content.decode("utf-8")

        import xml.dom.minidom
        dom = xml.dom.minidom.parseString(xmldata)
        pretty_xml_as_string = dom.toprettyxml()

        from pygments import highlight
        from pygments.lexers import XmlLexer
        from pygments.formatters import TerminalFormatter
        #
        # lexer = get_lexer_by_name("XML", stripall=True)
        # formatter = get_formatter_by_name("Terminal")
        # result = highlight(pretty_xml_as_string, lexer, formatter)
        result = highlight(xmldata, XmlLexer(), TerminalFormatter())

        print(result)
        # print(response.content.decode("utf-8"))
        return xmltodict.parse(response.content)

    def get_NodeStatusUVEList(self):
        data = self.Snh_SandeshUVECacheReq(tname='NodeStatus')
        return NodeStatusUVEList(data['__NodeStatusUVE_list'])


class NodeStatusUVEList(IntrospectData):
    def __init__(self, obj):
        super(NodeStatusUVEList, self).__init__(obj)
        self.NodeStatusUVE = \
            self._wrap_in_list(NodeStatusUVE, self.obj['NodeStatusUVE'])


class NodeStatusUVE(IntrospectData):
    def __init__(self, obj):
        super(NodeStatusUVE, self).__init__(obj)
        self.NodeStatus = \
            self._wrap_in_list(NodeStatus, self.obj['data']['NodeStatus'])
