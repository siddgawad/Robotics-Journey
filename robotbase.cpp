#include <iostream>
#include <string>

class RobotBase{
    public:
    std::string name;

    RobotBase(std::string& name_params){
        name = name_params;
    }

    void report() const {
        std::cout<<"Name : " << name;
    }
};

class MobileRobot : public RobotBase {
    public: double x, y;

    MobileRobot(std::string& name, double x, double y):RobotBase(name){
        name = name;
        x+= x;
        y+= y;

    }
};