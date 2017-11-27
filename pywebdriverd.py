#!/usr/bin/env python

from pywebdriver import app, config, drivers

def main():
    host = config.get('flask', 'host')
    port = config.getint('flask', 'port')
    debug = config.getboolean('flask', 'debug') 
    if config.getboolean('application', 'print_status_start'):
        if 'escpos' in drivers:
            drivers['escpos'].push_task('printstatus')
    app.run(host=host, port=port, debug=debug)

# Run application
if __name__ == '__main__':
    main()
