#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f = cgi.FieldStorage()
data = f.getvalue("x")
values = data.split()

if values[0] == "1":

    deployment_name = values[2]
    image = values[1]
    cmd = "kubectl create deployment "+deployment_name+" --image="+image
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)

elif values[0] == "2":

    pod_name = values[2]
    image = values[1]
    cmd = "kubectl run " + pod_name +" --image= "+image
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)

elif values[0] == "3":

    deployment_name = values[2]
    port = values[1]
    cmd = "kubectl expose deployment " + deployment_name +" --port="+ port +" --type= "+NodePort
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)

elif values[0] == "4":

    deployment_name = values[2]
    replica = values[1]
    cmd = "kubectl scale deployment " + deployment_name +" --replicas="+ replica
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)


elif values[0] == "5":

    cmd = "kubectl get pods "
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif values[0] == "6":

    cmd = "kubectl get svc "
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)


elif values[0] == "7":
    deployment_name = values[1]
    cmd = "kubectl describe svc "+ deployment_name
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)

elif values[0] == "8":

    deployment_name = values[1]
    cmd = "kubectl delete deployment "+deployment_name
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)

elif values[0] == "9":

    cmd = "kubectl delete all --all "
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)