from optparse import OptionParser
from actuation.scenarios.abstract import AbstractSimulation
from actuation.impl.resources import LampResource, LightResource
from actuation.utils.files import append_slash_if_absent
from actuation.impl.mock.light_rest_provider import LightProviderRESTMock
from actuation.impl.mock.light_rest_consumer import LightConsumerRESTMock


class OnlyRESTDevicesSimulator(AbstractSimulation):
    
    def __init__(self, input_folder, output_folder, reasoner):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.reasoner = reasoner
    
    @property    
    def lc(self):
        return self.nodes["consumer"]
    
    @lc.setter
    def lc(self, value):
        self.nodes["consumer"] = value
    
    @property    
    def lp(self):
        return self.nodes["provider"]
    
    @lp.setter
    def lp(self, value):
        self.nodes["provider"] = value    
    
    def configure(self):
        lamp_resource = LampResource( self.input_folder + "lamp_desc.n3" )
        light_resource = LightResource( self.input_folder + "light_get.n3",
                                        self.input_folder + "light_post.n3",
                                        self.input_folder + "light_get_ret.n3.tpl",
                                        self.output_folder )
        self.lp = LightProviderRESTMock( lamp_resource, light_resource )
        self.lc = LightConsumerRESTMock()
        self.lc.discover( self.lp )
    
    def execute(self):
        '''
        Executes the scenario where the consumer tries to change the light in the environment.
        '''
        # do sth
        pass
    
    def check(self):
        pass


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      help="Base directory where all the files used in the simulation are stored.")
    parser.add_option("-o", "--output", dest="output", default="/tmp",
                      help="Output folder where the processed results will be written.")
    parser.add_option("-e", "--euler", dest = "euler", default='../../../../',
                      help = "Path to Euler.jar")
    (options, args) = parser.parse_args()
    
    from actuation.proofs.reasoner import EulerReasoner
    reasoner = EulerReasoner( options.euler )
    
    sim = OnlyRESTDevicesSimulator( append_slash_if_absent( options.input ),
                                    append_slash_if_absent( options.output ),
                                    reasoner )
    sim.run()