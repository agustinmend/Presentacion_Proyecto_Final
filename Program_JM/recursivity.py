def reverse(word, revword, i):
    if not word:  # Handles both None and empty string
        return revword
    if i < 0:
        return revword
    else:
        revword += word[i]
        return reverse(word, revword, i - 1)