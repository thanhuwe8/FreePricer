from Utils.Vars import EquityBumpSize



class EquityOption:
    
    #? Use injection dependency for parameter "model"
    def calculate(self, Price, ValuationDate, DFcurve, Dividendcurve, model):
        print("Calculate method")
        return(-0.0001)

    #? Full revaluation based on EquityBumpSize
    def delta(self, Price, ValuationDate, DFcurve, Dividendcurve, model):
        
        current_value = self.calculate(Price, ValuationDate, DFcurve, Dividendcurve, model)
        bumped_value = self.calculate(Price + EquityBumpSize, ValuationDate, DFcurve, Dividendcurve, model)
        
        