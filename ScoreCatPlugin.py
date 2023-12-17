
import pickle
import PyIO
import pandas as pd
import PyPluMA

class ScoreCatPlugin:
    def input(self, inputfile):
       self.parameters = PyIO.readParameters(inputfile)
    def run(self):
       pass
    def output(self, outputfile):
       out_file = PyPluMA.prefix()+"/"+self.parameters["out_file"]
       scorefile = PyPluMA.prefix()+"/"+self.parameters["scorefile"]
       ppifile = PyPluMA.prefix()+"/"+self.parameters["ppifile"]
       quality = self.parameters["quality"]
       score = self.parameters["score"]
       ppi = self.parameters["ppi"]

       scorehandle = open(scorefile, 'rb')
       output = pickle.load(scorehandle)
       ppi_list = PyIO.readSequential(ppifile)


       scores_df = pd.read_csv(out_file)
       scores_df = scores_df[[quality,score,ppi]]
       scores_df_native = pd.DataFrame({quality: [0]*len(output), score:output, ppi:ppi_list})
       scores_df = pd.concat([scores_df, scores_df_native], ignore_index=True)

       scores_df.to_csv(outputfile)


