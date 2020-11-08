from examples import custom_style_dope
import questionary

if __name__ == "__main__":
    toppings = (
        questionary.checkbox(
            "Select toppings",
            choices=["foo", "bar", "bazz"],
            validate=lambda a: (len(a) != 0, "You must select at least one topping"),
            style=custom_style_dope,
        ).ask()
        or []
    )

    print(f"Alright let's go mixing some {' and '.join(toppings)} 🤷‍♂️.")
