# tf-introspect-client

TungstenFabric introspect client bindings

## Example

```
from tf_introspect_client.lib.introspect_client import IntrospectClient

ic = IntrospectClient(ip=<introspect_ip>, port=<introspect_port>)
    ns = ic.get_NodeStatusUVEList()
    for status_uve in ns.NodeStatusUVE:
        process_status = status_uve.NodeStatus[0].ProcessStatus[0]
        print(process_status.module_id)
        print(process_status.state)
```
