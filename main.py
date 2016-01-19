import engine
import system
import multiprocessing

systemEngine = engine.Engine(system.System())
systemEngine.start()
systemEngine.result()
