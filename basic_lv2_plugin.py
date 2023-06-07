import liblo, sys, time

try:
    server = liblo.ServerThread(33752, liblo.TCP)
except liblo.ServerError as err:
    print(err)
    sys.exit()

def fallback(path, args, types, src):
    print("Path '%s' (from '%s')" % (path, src.url))
    for a, t in zip(args, types):
        print("\t'%s': %s" % (t, a))

server.add_method(None, None, fallback)
server.start()
time.sleep(0.5)

# Registering with the carla instance so that we receive status back
print("Register with {}".format(server.url))
liblo.send("osc.tcp://127.0.0.1:22752", "/register", server.url)
time.sleep(0.5)

# add_plugin <request id> <binary type (2==posix 64)> <plugin type (4==lv2)> <filename> <name> <label (uri, required for lv2)> <unique plugin id> <options>
liblo.send("osc.tcp://127.0.0.1:22752", "/ctrl/add_plugin", 1234, 2, 4, "(null)", "(null)", "http://distrho.sf.net/examples/Info", 0, 0)
time.sleep(10)
# remove_plugin <request id> <unique plugin id>
liblo.send("osc.tcp://127.0.0.1:22752", "/ctrl/remove_plugin", 1234, 0)

time.sleep(0.5)
liblo.send("osc.tcp://127.0.0.1:22752", "/unregister", "127.0.0.1")
