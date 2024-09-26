import pyshark
import pandas as pd

def extract_tls_info(pcap_file):
    cap = pyshark.FileCapture(pcap_file, display_filter='tls')

    tls_info = {
        'tls_versions': [],
        'client_hellos': [],
        'server_hellos': [],
        'certificates': []
    }

    for pkt in cap:
        if 'tls' in pkt:
            tls_layer = pkt.tls
            # Extract TLS Version
            if hasattr(tls_layer, 'record_version'):
                tls_info['tls_versions'].append(tls_layer.record_version)
            
            # Extract ClientHello
            if hasattr(tls_layer, 'handshake_type') and tls_layer.handshake_type == '1':  # Handshake Type 1 is ClientHello
                client_hello_info = {
                    'version': tls_layer.handshake_version,
                    'random': tls_layer.handshake_random
                }
                tls_info['client_hellos'].append(client_hello_info)
            
            # Extract ServerHello
            if hasattr(tls_layer, 'handshake_type') and tls_layer.handshake_type == '2':  # Handshake Type 2 is ServerHello
                server_hello_info = {
                    'version': tls_layer.handshake_version,
                    'random': tls_layer.handshake_random
                }
                tls_info['server_hellos'].append(server_hello_info)
            
            # Extract Certificates
            if hasattr(tls_layer, 'handshake_certificate'):
                tls_info['certificates'].append(tls_layer.handshake_certificate)

    return tls_info

def save_to_excel(tls_info, output_file):
    # Convert TLS Versions to DataFrame
    tls_versions_df = pd.DataFrame(tls_info['tls_versions'], columns=['TLS Version'])

    # Convert ClientHellos to DataFrame
    client_hellos_df = pd.DataFrame(tls_info['client_hellos'])

    # Convert ServerHellos to DataFrame
    server_hellos_df = pd.DataFrame(tls_info['server_hellos'])

    # Convert Certificates to DataFrame
    certificates_df = pd.DataFrame(tls_info['certificates'], columns=['Certificate'])

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        tls_versions_df.to_excel(writer, sheet_name='TLS Versions', index=False)
        client_hellos_df.to_excel(writer, sheet_name='Client Hellos', index=False)
        server_hellos_df.to_excel(writer, sheet_name='Server Hellos', index=False)
        certificates_df.to_excel(writer, sheet_name='Certificates', index=False)

# Contoh penggunaan
pcap_file = 'tls_fix.pcapng'
output_file = 'tls_info.xlsx'

tls_info = extract_tls_info(pcap_file)
save_to_excel(tls_info, output_file)

print(f"Hasil ekstraksi TLS telah disimpan ke {output_file}")
