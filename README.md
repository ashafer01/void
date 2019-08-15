# void.py

This was an exercise in creating a None-like object that tries to do nothing
successfully. Of course in many cases this is pointless, as doing nothing
successfully will just lead to different errors a little later on, but
nonetheless it seemed like an interesting task.

While I probably will make a more specific solution (and not actually use this),
the idea to do this occurred to me while thinking about how to have an
optionally configured storage backend within an application. Briefly I thought
it would be convenient to have a placeholder for the database object that would
just skip over the cursor() context manager calls where all the database logic
lives.

Again, in practice, this is probably a good solution for almost nothing. Don't
use it without heavy modification.

This will most likely only ever see the one commit in terms of maintenance.
Don't bother opening issues. PR's are welcome.
