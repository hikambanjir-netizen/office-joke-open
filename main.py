"""Office Joke Open entry: writes one single-line office joke to entry.txt."""

import os

JOKE = (
    "I hit reply-all to beg everyone to stop replying all, and now 400 "
    "coworkers, two printers, and the CEO's out-of-office are replying "
    "all to agree with me."
)


def _check_joke(text: str) -> str:
    """Guard the gate rules: one line, 1 to 200 chars, not blank."""
    cleaned = text.strip()
    assert cleaned, "joke must not be blank"
    assert "\n" not in cleaned and "\r" not in cleaned, "joke must be one line"
    assert len(cleaned) <= 200, "joke must fit the 200 character limit"
    return cleaned


def main() -> None:
    joke = _check_joke(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(joke)


if __name__ == "__main__":
    main()
