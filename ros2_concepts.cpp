#include <iostream>
#include <string>
#include <optional>


class Battery {
    public: double soc,capacity_wh;

    Battery(const double capacity, std::optional<double>soc_state){
    capacity_wh = capacity;
    soc_state = soc;
    }

    void discharge(double power_w,double duration_h){
        soc = soc-(power_w*duration_h);
    }

    void report() const {
        std::cout<< "Battery: SOC = " << soc << "% \n"; 
    }

};