import sys
import subprocess

input_file= sys.argv[1]
seconds= sys.argv[2]
num_pieces= sys.argv[3]

for i in range(num_pieces):
    num= i* seconds
    output= "output/{0}.wav".format(i)
    s=["ffmpeg","-i",str(input_file),"-ss",str(num),"-t",str(seconds),"-acodec","copy",output]
    subprocess.call(s)