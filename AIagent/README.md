## 对于LangGraph那份代码使用需要注意的点

运行时记得在导包时`os.environ["TAVILY_API_KEY"] = "your-api-key"`
获得`TAVILY_API_KEY`的方法我记载到了博客https://blog.csdn.net/d_i_o_jojo/article/details/146106799?spm=1001.2014.3001.5501

下面这个指令可以用来快速复制当前虚拟环境生成requirements.txt
```bash
pip freeze > requirements.txt
```

在进行stream构建时，有一个包缺失了，`from langgraph.checkpoint.sqlite import SqliteSaver`，可以使用以下命令来安装
```bash
pip install langgraph-checkpoint-sqlite==2.0.3
```
