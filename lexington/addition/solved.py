import angr,sys

def main():
    proj = angr.Project('./addition')
    init_state = proj.factory.entry_state()
    simulation = proj.factory.simgr(init_state)

    simulation.explore(find=is_successful, avoid=should_abort)

    if simulation.found:
        solution = simulation.found[0]
        print('flag: ', solution.posix.dumps(sys.stdin.fileno()))
    else:
        print('no flag')

def is_successful(state):
    return b"correct" in state.posix.dumps(sys.stdout.fileno())

# set disexpected function
def should_abort(state):
    return b"wrong" in state.posix.dumps(sys.stdout.fileno())

if __name__ == '__main__':
    main()
