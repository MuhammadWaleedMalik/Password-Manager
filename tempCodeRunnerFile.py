    ok=messagebox.askokcancel(title="Cheking",message=f"Email:f{Email}\n Name: f{Name} \n Password: {passw} \n Is it Correct Info")
        if ok:
            dic={"Name":f"{Name}","Email":f"{Email}","Password":f"{passw}"}
            lis.append(dic)
            var=pd.DataFrame(lis)
            var.to_csv("DATA.csv")
