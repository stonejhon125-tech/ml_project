import threading
import time
import queue

class DebateSimulator:
    def __init__(self, dilemma, values):
        self.dilemma = dilemma
        self.values = values
        self.pro_args = []
        self.con_args = []
        self.log_queue = queue.Queue()

    def pro_agent(self):
        """Simulates an agent arguing for the action."""
        # Simple logical simulation (mock arguments)
        time.sleep(1)
        arg = f"PRO: Implementing this aligns with innovation. Values considered: {self.values}"
        self.pro_args.append(arg)
        self.log_queue.put(arg)
        time.sleep(1)
        arg = "PRO: Financial growth is likely positive."
        self.pro_args.append(arg)
        self.log_queue.put(arg)

    def con_agent(self):
        """Simulates an agent arguing against the action."""
        time.sleep(1.5)
        arg = f"CON: Warning! Risks associated with {self.dilemma[:20]}... might be high."
        self.con_args.append(arg)
        self.log_queue.put(arg)
        time.sleep(1)
        arg = "CON: Potential privacy violations detected."
        self.con_args.append(arg)
        self.log_queue.put(arg)

    def run_debate(self):
        t1 = threading.Thread(target=self.pro_agent)
        t2 = threading.Thread(target=self.con_agent)
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
        
        return list(self.log_queue.queue)
