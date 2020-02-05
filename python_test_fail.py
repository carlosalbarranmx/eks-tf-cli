#!/usr/bin/env python3

import contextlib
import io
import unittest
import  subprocess
import os, tempfile

def readcmd(cmd):
    ftmp = tempfile.NamedTemporaryFile(suffix='.out', prefix='tmp', delete=False)
    fpath = ftmp.name
    if os.name=="nt":
        fpath = fpath.replace("/","\\") 
    ftmp.close()
    os.system(cmd + " > " + fpath)
    data = ""
    with open(fpath, 'r') as file:
        data = file.read()
        file.close()
    os.remove(fpath)
    return data


class LogProcessorTests(unittest.TestCase):

    def setUp(self):
        self.var = '<h1> Hello World </h1>'

    def test_var_value(self):
        print('Running Python tests...')
        print('Validating Hello World Response for Flask Service IP:')
        output = readcmd("export IP=$(kubectl describe svc/flask-example | grep IP: | awk '{print $2;}'); kubectl exec -it curl-0 curl $IP")
        print(output)  
        #outputcurl = "kubectl exec -it curl-0 curl " + output
        #outputcurl = readcmd(outputcurl)
        #print(outputcurl)
        self.assertEqual(self.var, '<h1> Hello Flugel</h1>')
        print('-----------------------')
        print(output) 
        


if __name__ == '__main__':
    # find all tests in this module
    import __main__
    suite = unittest.TestLoader().loadTestsFromModule(__main__)
    with io.StringIO() as buf:
        # run the tests
        with contextlib.redirect_stdout(buf):
            unittest.TextTestRunner(stream=buf).run(suite)
        # process (in this case: print) the results
        print('*** CAPTURED TEXT***:\n%s' % buf.getvalue())

