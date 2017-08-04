scenarios = []
when_step = []
then_step = "  Then the user [X will happen or is expected]"
steps = []


def create_feature_steps():
    var1 = []
    var2 = []
    var3 = []
    for a in var3:
        for b in var2:
            for c in var1:
                scenarios.append("User can " + b + " to a " + c + " within " + a)
                when_step.append("  When a user " + b + " to a " + c + " in " + a)


def create_temp_steps():
    for scenario in scenarios:
        print("@When(\"^" + scenario + "$\")\n" + "public void " + scenario.replace(" ", "_") + "() throws Throwable\n" + "")
        print()


def display_item():
    top_scenarios = "@skip\n Scenario: "
    print("Feature: \n")
    for i in range(len(scenarios)):
        print(top_scenarios + scenarios[i])
        print(when_step[i])
        print(then_step)
        print()
