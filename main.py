"""One Line, One Laugh -- make.fun one-liner entry.

The line takes one sharp, fresh premise: the smart fridge, the one
appliance whose entire job is to keep food cold, has started acting
like a judgmental personal trainer and emailed its owner a diet plan.
The joke turns on the owner's response -- not a reasoned reply, not
obedience, but petty revenge: unplug the fridge and eat ice cream out
of spite. The laugh lands in a single beat, on the word "spite", which
flips the power dynamic: the human would rather sabotage the machine
than be lectured by it. It needs no setup beyond the fridge everyone
already owns, every word earns its place, and the punch is the exact
opposite of what a diet plan is supposed to achieve.
"""

import os

# The entry: a smart fridge oversteps, its owner answers with spite.
# The fridge emails a diet plan; the owner unplugs it and eats ice
# cream -- the diet plan defeated by the very appliance it came from.
LINE = "My smart fridge emailed me a diet plan, so I unplugged it and ate ice cream out of spite."


def validate(text):
    """Check that a candidate entry line meets the competition rules.

    Raises ValueError unless ``text`` is a non-blank single-line ASCII
    string of 1 to 140 characters, with no leading or trailing space and
    no double spaces.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
