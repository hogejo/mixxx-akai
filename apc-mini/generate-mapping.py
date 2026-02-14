import textwrap

output_file = open('apc-mini-2-decks.midi.xml', 'w')

# deck -> deck_offset
decks = {1: 0, 2: 1}

# hotcue -> hotcue_offset
hotcues = {
    1: 8, 2: 9, 3: 10, 4: 11,
    5: 0, 6: 1, 7: 2, 8: 3
}

pad_rows = {
    "beatjump": 0x20,
    "beatloop": 0x30,
    "hotcue": 0x10,
    "intro": 0x08,
    "play": 0x00,
    "sync": 0x28,
}

colours = {
    "back": 0x06,
    "back_press": 0x05,
    "beatloop": 0x54,
    "cue": 0x09,
    "cue_set": 0x3C,
    "forward": 0x16,
    "forward_press": 0x57,
    "hotcue": 0x2D,
    "intro": 0x25,
    "outro": 0x4F,
    "play": 0x15,
    "press": 0x02,
    "reverse": 0x05,
    "sync": 0x60,
    "sync_leader": 0x54,
}


def write(string):
    if "\n" in string:
        string = textwrap.dedent(string)
    string = string.strip(" \t\n\r")
    string += "\n"
    while "\n\n" in string:
        string = string.replace("\n\n", "\n")
    output_file.write(string)


def h(x):
    return hex(x)[2:].upper().rjust(2, '0')


def comment(string):
    write(f"<!-- {string} -->")


def header(name: str, author: str, description: str, wiki: str):
    write(f"""
    <?xml version='1.0' encoding='utf-8'?>
    <MixxxControllerPreset mixxxVersion="" schemaVersion="1">
    <info>
    <name>{name}</name>
    <author>{author}</author>
    <description>{description}</description>
    <wiki>{wiki}</wiki>
    </info>""")


def footer():
    write("</MixxxControllerPreset>")


def begin_settings():
    write("<settings>")


def end_settings():
    write("</settings>")


def setting(variable: str, variable_type: str, label: str, description: str, default: str):
    write(f"""
    <option variable="{variable}" type="{variable_type}" label="{label}" default="{default}">
        <description>{description}</description>
     </option>""")


def begin_controller(scriptfiles: dict[str, str] = {}):
    write("""<controller id="">""")
    if len(scriptfiles.items()) > 0:
        write("<scriptfiles>")
        for filename, prefix in scriptfiles.items():
            write(f"""<file filename="{filename}" functionprefix="{prefix}"/>""")
        write("</scriptfiles>")
    else:
        write("<scriptfiles/>")


def end_controller():
    write("</controller>")


def begin_controls():
    write("<controls>")


def end_controls():
    write("</controls>")


def control(
    group: str,
    key: str,
    description: str,
    status: int,
    midino: int,
    options: str = "normal",
    push: bool = False
):
    options = f"<{options}/>"
    write(f"""
    <control>
        <group>{group}</group>
        <key>{key}</key>
        <description>{description}</description>
        <status>{hex(status)}</status>
        <midino>{hex(midino)}</midino>
        <options>{options}</options>
    </control>""")
    if push:
        control(group, key, description + " (released)", 0x80, midino, options="normal")


def begin_outputs():
    write("<outputs>")


def end_outputs():
    write("</outputs>")


def output(
    group: str,
    key: str,
    status: int,
    midino: int,
    on: int = 1,
    off: int = 0,
    minimum: int = 1,
    maximum: int = 1000,
):
    write(f"""
    <output>
        <group>{group}</group>
        <key>{key}</key>
        <status>{hex(status)}</status>
        <midino>{hex(midino)}</midino>
        <on>{hex(on)}</on>
        <off>{hex(off)}</off>
        <minimum>{minimum}</minimum>
        <maximum>{maximum}</maximum>
    </output>""")


header(
    name="Akai Pro APC mini - 2 Decks",
    author="hogejo",
    description="Mapping for Akai Pro APC mini with two decks. There is no filter control, except EQ.",
    wiki="https://github.com/hogejo/mixxx-akai"
)

begin_settings()
setting(
    variable="eqClampingEnabled",
    variable_type="boolean",
    label="Clamp EQ faders to 0 - 0.5",
    description="Clamp EQ faders to 0 - 0.5",
    default="true"
)
end_settings()

begin_controller(
    scriptfiles={
        "apc-mini.js": "APCMini",
    }
)

# Controls (events)
begin_controls()
control(
    group="[Master]",
    key="gain",
    description="Master / gain",
    status=0xB0,
    midino=0x38
)
comment("DECKS")
for deck, deck_offset in decks.items():
    comment(f"START: DECK {deck}")
    # pads: loop
    control(
        group=f"[Channel{deck}]", key="beatloop_activate",
        description=f"Deck {deck} / beatloop",
        status=0x90, midino=pad_rows["beatloop"] + 8 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="beatlooproll_activate",
        description=f"Deck {deck} / temporary beatloop",
        status=0x90, midino=pad_rows["beatloop"] + 9 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="loop_havle",
        description=f"Deck {deck} / halve beatloop size",
        status=0x90, midino=pad_rows["beatloop"] + 10 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="loop_double",
        description=f"Deck {deck} / double beatloop size",
        status=0x90, midino=pad_rows["beatloop"] + 11 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="reloop_toggle",
        description=f"Deck {deck} / toggle reloop",
        status=0x90, midino=pad_rows["beatloop"] + 0 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="loop_in",
        description=f"Deck {deck} / loop in",
        status=0x90, midino=pad_rows["beatloop"] + 1 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="loop_out",
        description=f"Deck {deck} / loop out",
        status=0x90, midino=pad_rows["beatloop"] + 2 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="loop_anchor",
        description=f"Deck {deck} / toggle loop anchor",
        status=0x90, midino=pad_rows["beatloop"] + 3 + (4 * deck_offset),
        push=True
    )
    # pads: sync
    control(
        group=f"[Channel{deck}]", key="rate_perm_down_small",
        description=f"Deck {deck} / decrease BPM",
        status=0x90, midino=pad_rows["sync"] + 0 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="rate_perm_up_small",
        description=f"Deck {deck} / increase BPM",
        status=0x90, midino=pad_rows["sync"] + 1 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="sync_enabled",
        description=f"Deck {deck} / sync",
        status=0x90, midino=pad_rows["sync"] + 2 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="sync_leader",
        description=f"Deck {deck} / sync leader",
        status=0x90, midino=pad_rows["sync"] + 3 + (4 * deck_offset)
    )
    # pads: beatjump
    control(
        group=f"[Channel{deck}]", key="beatjump_backward",
        description=f"Deck {deck} / beatjump forward",
        status=0x90, midino=pad_rows["beatjump"] + 0 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="beatjump_forward",
        description=f"Deck {deck} / beatjump backward",
        status=0x90, midino=pad_rows["beatjump"] + 1 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="beatjump_size_halve",
        description=f"Deck {deck} / halve beatjump size",
        status=0x90, midino=pad_rows["beatjump"] + 2 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key="beatjump_size_double",
        description=f"Deck {deck} / double beatjump size",
        status=0x90, midino=pad_rows["beatjump"] + 3 + (4 * deck_offset),
        push=True
    )
    # pads: intro
    control(
        group=f"[Channel{deck}]", key=f"intro_start_activate",
        description=f"Deck {deck} / intro start activate",
        status=0x90, midino=pad_rows["intro"] + 0 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key=f"intro_end_activate",
        description=f"Deck {deck} / intro end activate",
        status=0x90, midino=pad_rows["intro"] + 1 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key=f"outro_start_activate",
        description=f"Deck {deck} / outro start activate",
        status=0x90, midino=pad_rows["intro"] + 2 + (4 * deck_offset),
        push=True
    )
    control(
        group=f"[Channel{deck}]", key=f"outro_end_activate",
        description=f"Deck {deck} / outro end activate",
        status=0x90, midino=pad_rows["intro"] + 3 + (4 * deck_offset),
        push=True
    )
    # pads: hotcues
    for hotcue, hotcue_offset in hotcues.items():
        control(
            group=f"[Channel{deck}]", key=f"hotcue_{hotcue}_activate",
            description=f"Deck {deck} / hotcue {hotcue} / activate",
            status=0x90, midino=pad_rows["hotcue"] + hotcue_offset + (4 * deck_offset),
            push=True
        )
    # pads: play, cue, reverse
    control(
        group=f"[Channel{deck}]", key="play",
        description=f"Deck {deck} / play/pause",
        status=0x90, midino=pad_rows["play"] + 0 + (4 * deck_offset)
    )
    control(
        group=f"[Channel{deck}]", key="cue_goto",
        description=f"Deck {deck} / go to CUE",
        status=0x90, midino=pad_rows["play"] + 1 + (4 * deck_offset)
    )
    control(
        group=f"[Channel{deck}]", key="cue_set",
        description=f"Deck {deck} / set CUE",
        status=0x90, midino=pad_rows["play"] + 2 + (4 * deck_offset)
    )
    control(
        group=f"[Channel{deck}]", key="reverse",
        description=f"Deck {deck} / reverse pressed",
        status=0x90, midino=pad_rows["play"] + 3 + (4 * deck_offset),
        push=True
    )
    # end of pads, start of faders
    control(
        group=f"[Channel{deck}]", key="volume",
        description="Deck {deck} / volume",
        status=0xB0, midino=0x30 + (4 * deck_offset)
    )
    control(
        group=f"[Channel{deck}]", key="pfl",
        description=f"Deck {deck} / headphone",
        status=0x90, midino=0x64 + (4 * deck_offset)
    )
    for eq, name in {1: "low", 2: "mid", 3: "high"}.items():
        control(
            group=f"[EqualizerRack1_[Channel{deck}]_Effect1]", key=f"button_parameter{eq}",
            description=f"Deck {deck} / EQ {name} on/off",
            status=0x90, midino=0x64 + eq + (4 * deck_offset),
        )
        control(
            group=f"[EqualizerRack1_[Channel{deck}]_Effect1]", key=f"APCMini.clampEQ.deck{deck}.eq{eq}",
            description=f"Deck {deck} / EQ {name} level",
            status=0xB0, midino=0x30 + eq + (4 * deck_offset),
            options="script-binding"
        )
    comment(f"END: DECK {deck}")
end_controls()

# Outputs
begin_outputs()
for deck, deck_offset in decks.items():
    comment(f"DECK {deck}")
    # beatloop
    output(
        group=f"[Channel{deck}]", key="loop_enabled",
        status=0x96, midino=pad_rows["beatloop"] + 8 + (4 * deck_offset),
        on=colours["beatloop"],
    )
    output(
        group=f"[Channel{deck}]", key="beatlooproll_activate",
        status=0x96, midino=pad_rows["beatloop"] + 9 + (4 * deck_offset),
        on=colours["beatloop"],
    )
    output(
        group=f"[Channel{deck}]", key="loop_halve",
        status=0x96, midino=pad_rows["beatloop"] + 10 + (4 * deck_offset),
        on=colours["press"],
    )
    output(
        group=f"[Channel{deck}]", key="loop_double",
        status=0x96, midino=pad_rows["beatloop"] + 11 + (4 * deck_offset),
        on=colours["press"],
    )
    output(
        group=f"[Channel{deck}]", key="reloop_toggle",
        status=0x96, midino=pad_rows["beatloop"] + 0 + (4 * deck_offset),
        on=colours["press"],
    )
    output(
        group=f"[Channel{deck}]", key="loop_in",
        status=0x96, midino=pad_rows["beatloop"] + 1 + (4 * deck_offset),
        on=colours["press"],
    )
    output(
        group=f"[Channel{deck}]", key="loop_out",
        status=0x96, midino=pad_rows["beatloop"] + 2 + (4 * deck_offset),
        on=colours["press"],
    )
    output(
        group=f"[Channel{deck}]", key="loop_anchor",
        status=0x96, midino=pad_rows["beatloop"] + 3 + (4 * deck_offset),
        on=colours["back"], off=colours["forward"],
    )
    # rate, sync
    output(
        group=f"[Channel{deck}]", key="rate_perm_down_small",
        status=0x96, midino=pad_rows["sync"] + 0 + (4 * deck_offset),
        on=colours["back_press"], off=colours["back"],
    )
    output(
        group=f"[Channel{deck}]", key="rate_perm_up_small",
        status=0x96, midino=pad_rows["sync"] + 1 + (4 * deck_offset),
        on=colours["forward_press"], off=colours["forward"],
    )
    output(
        group=f"[Channel{deck}]", key="sync_enabled",
        status=0x96, midino=pad_rows["sync"] + 2 + (4 * deck_offset),
        on=colours["sync"],
    )
    output(
        group=f"[Channel{deck}]", key="sync_leader",
        status=0x96, midino=pad_rows["sync"] + 3 + (4 * deck_offset),
        on=colours["sync_leader"],
    )
    # beatjump
    output(
        group=f"[Channel{deck}]", key="beatjump_backward",
        status=0x96, midino=pad_rows["beatjump"] + 0 + (4 * deck_offset),
        on=colours["back_press"], off=colours["back"],
    )
    output(
        group=f"[Channel{deck}]", key="beatjump_forward",
        status=0x96, midino=pad_rows["beatjump"] + 1 + (4 * deck_offset),
        on=colours["forward_press"], off=colours["forward"],
    )
    output(
        group=f"[Channel{deck}]", key="beatjump_size_halve",
        status=0x96, midino=pad_rows["beatloop"] + 2 + (4 * deck_offset),
        on=colours["press"],
    )
    output(
        group=f"[Channel{deck}]", key="beatjump_size_double",
        status=0x96, midino=pad_rows["beatloop"] + 3 + (4 * deck_offset),
        on=colours["press"],
    )
    # intro/outro
    output(
        group=f"[Channel{deck}]", key="intro_start_enabled",
        status=0x96, midino=pad_rows["intro"] + 0 + (4 * deck_offset),
        on=colours["intro"],
    )
    output(
        group=f"[Channel{deck}]", key="intro_end_enabled",
        status=0x96, midino=pad_rows["intro"] + 1 + (4 * deck_offset),
        on=colours["intro"],
    )
    output(
        group=f"[Channel{deck}]", key="outro_start_enabled",
        status=0x96, midino=pad_rows["intro"] + 2 + (4 * deck_offset),
        on=colours["outro"],
    )
    output(
        group=f"[Channel{deck}]", key="outro_end_enabled",
        status=0x96, midino=pad_rows["intro"] + 3 + (4 * deck_offset),
        on=colours["outro"],
    )
    # Hotcues are lit from JS
    # for hotcue, hotcue_offset in hotcues.items():
    #     output(
    #         group=f"[Channel{deck}]", key=f"hotcue_{hotcue}_status",
    #         status=0x96, midino=0x08 + hotcue_offset + (4 * deck_offset),
    #         on=colours["hotcue"],
    #     )
    # play/cue/reverse
    output(
        group=f"[Channel{deck}]", key="play_indicator",
        status=0x96, midino=pad_rows["play"] + 0 + (4 * deck_offset),
        on=colours["play"],
    )
    output(
        group=f"[Channel{deck}]", key="cue_indicator",
        status=0x96, midino=pad_rows["play"] + 1 + (4 * deck_offset),
        on=colours["cue"],
    )
    output(
        group=f"[Channel{deck}]", key="cue_indicator",
        status=0x96, midino=pad_rows["play"] + 2 + (4 * deck_offset),
        on=colours["cue_set"],
    )
    output(
        group=f"[Channel{deck}]", key="reverse",
        status=0x96, midino=pad_rows["play"] + 3 + (4 * deck_offset),
        on=colours["reverse"],
    )
    # buttons
    output(
        group=f"[Channel{deck}]", key="pfl",
        status=0x90, midino=0x64 + (4 * deck_offset),
    )
    for eq, name in {1: "low", 2: "mid", 3: "high"}.items():
        output(
            group=f"[EqualizerRack1_[Channel{deck}]_Effect1]", key=f"button_parameter{eq}",
            status=0x90, midino=0x64 + eq + (4 * deck_offset),
        )

end_outputs()
end_controller()
footer()
