'''
Created on Feb 25, 2011

Network Connection Module will handle the interfacing
between the client bot application and the MTGO Bot server

@author: Darkray16
'''

if __name__ == '__main__':
    import urllib, urllib2
    
    try:
        import json
    except ImportError:
        import simplejson as json
    
    mtgo_bot_id = raw_input("id: ")
    mtgo_bot_pass = raw_input("pass: ")    
    
    mtgo_id = raw_input("sn: ")
    mtgo_pass = raw_input("pass: ")
   
    check = True
    while check:
        port_input = raw_input("Please enter port number(higher than 49152):")
        try:
            port_number = int(port_input)
            check = (port_number < 49152)
        except:
            check = True
    
    
    params = {'bot_id':mtgo_bot_id,
              'bot_password':mtgo_bot_pass,
              'mtgo_id':mtgo_id,
              'mtgo_pass':mtgo_pass}
    
    import socket
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    MAX = 65535
    PORT = port_number
     
    s.bind(('127.0.0.1', PORT))
    print 'starting client'
    s.sendto('bot_id: %s, bot_pass: %s, mtgo_id: %s, mtgo_pass: %s' % (mtgo_bot_id, mtgo_bot_pass, mtgo_id, mtgo_pass), ('127.0.0.1', 1060))
    data = s.recv(MAX)
    print 'server says ', repr(data)
    
    