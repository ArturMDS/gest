from militares.models import Militar
from subunidades.models import Subunidade
from quarteis.models import Quartel


def troca_su(id_su, id_mil):
    militar = Militar.objects.get(id=id_mil)
    id_quartel = militar.unidade.id
    subunidade = Subunidade.objects.get(id=id_su)
    unidade = Quartel.objects.get(id=id_quartel)
    if militar.subunidade:
        if militar.subunidade != subunidade:
            if militar.pessoa in militar.subunidade.acesso_sgte.all():
                militar.subunidade.acesso_sgte.remove(militar.pessoa)
                militar.subunidade.save()
            if militar.pessoa in militar.subunidade.acesso_encmat.all():
                militar.subunidade.acesso_encmat.remove(militar.pessoa)
                militar.subunidade.save()
            if militar.pessoa in militar.subunidade.oficiais.all():
                militar.subunidade.oficiais.remove(militar.pessoa)
                militar.subunidade.save()
            if militar.pessoa in militar.subunidade.quadros.all():
                militar.subunidade.quadros.remove(militar.pessoa)
                militar.subunidade.save()
            militar.subunidade = subunidade
            militar.save()
            if (militar.posto_grad != "Cabo") and ("Soldado" not in militar.posto_grad) and (
                    militar.posto_grad != "Conscrito"):
                if militar.pessoa not in unidade.quadros.all():
                    unidade.quadros.add(militar.pessoa)
                    unidade.save()
            if "Coronel" in militar.posto_grad:
                if militar.pessoa not in unidade.oficiais.all():
                    unidade.oficiais.add(militar.pessoa)
                    unidade.save()
            elif (militar.posto_grad == "Major") or (militar.posto_grad == "Capitão"):
                if militar.pessoa not in unidade.oficiais.all():
                    unidade.oficiais.add(militar.pessoa)
                    unidade.save()
            elif " Tenente" in militar.posto_grad:
                if militar.pessoa not in unidade.oficiais.all():
                    unidade.oficiais.add(militar.pessoa)
                    unidade.save()
            elif "à" in militar.posto_grad:
                if militar.pessoa not in unidade.oficiais.all():
                    unidade.oficiais.add(militar.pessoa)
                    unidade.save()
            elif "Sargento" in militar.posto_grad:
                if militar.pessoa not in subunidade.quadros.all():
                    subunidade.quadros.add(militar.pessoa)
                    subunidade.save()
            elif militar.posto_grad == "Subtenente":
                if militar.pessoa not in subunidade.quadros.all():
                    subunidade.quadros.add(militar.pessoa)
                    subunidade.save()
            else:
                pass
    else:
        militar.subunidade = subunidade
        militar.save()
        if (militar.posto_grad != "Cabo") and ("Soldado" not in militar.posto_grad) and (
                militar.posto_grad != "Conscrito"):
            if militar.pessoa not in unidade.quadros.all():
                unidade.quadros.add(militar.pessoa)
                unidade.save()
        if "Coronel" in militar.posto_grad:
            if militar.pessoa not in unidade.oficiais.all():
                unidade.oficiais.add(militar.pessoa)
                unidade.save()
        elif (militar.posto_grad == "Major") or (militar.posto_grad == "Capitão"):
            if militar.pessoa not in unidade.oficiais.all():
                unidade.oficiais.add(militar.pessoa)
                unidade.save()
        elif " Tenente" in militar.posto_grad:
            if militar.pessoa not in unidade.oficiais.all():
                unidade.oficiais.add(militar.pessoa)
                unidade.save()
        elif "à" in militar.posto_grad:
            if militar.pessoa not in unidade.oficiais.all():
                unidade.oficiais.add(militar.pessoa)
                unidade.save()
        elif "Sargento" in militar.posto_grad:
            if militar.pessoa not in subunidade.quadros.all():
                subunidade.quadros.add(militar.pessoa)
                subunidade.save()
        elif militar.posto_grad == "Subtenente":
            if militar.pessoa not in subunidade.quadros.all():
                subunidade.quadros.add(militar.pessoa)
                subunidade.save()
        else:
            pass


def acesso_om(id_mil, funcao):
    militar = Militar.objects.get(id=id_mil)
    om = militar.unidade
    if funcao == "cmt_om":
        om.cmt = militar.pessoa
        om.save()
    elif funcao == "s1":
        om.s1 = militar.pessoa
        om.save()
    elif funcao == "s2":
        om.s2 = militar.pessoa
        om.save()
    elif funcao == "s3":
        om.s3 = militar.pessoa
        om.save()
    elif funcao == "s4":
        om.s4 = militar.pessoa
        om.save()
    elif funcao == "cmt_su":
        militar.subunidade.cmt = militar.pessoa
        militar.subunidade.save()
    elif funcao == "aux_s1":
        om.acesso_s1.add(militar.pessoa)
        if militar.pessoa in om.acesso_s2.all():
            om.acesso_s2.remove(militar.pessoa)
        if militar.pessoa in om.acesso_s3.all():
            om.acesso_s3.remove(militar.pessoa)
        if militar.pessoa in om.acesso_s4.all():
            om.acesso_s4.remove(militar.pessoa)
        om.save()
    elif funcao == "aux_s2":
        om.acesso_s2.add(militar.pessoa)
        if militar.pessoa in om.acesso_s1.all():
            om.acesso_s1.remove(militar.pessoa)
        if militar.pessoa in om.acesso_s3.all():
            om.acesso_s3.remove(militar.pessoa)
        if militar.pessoa in om.acesso_s4.all():
            om.acesso_s4.remove(militar.pessoa)
        om.save()
    elif funcao == "aux_s3":
        om.acesso_s3.add(militar.pessoa)
        if militar.pessoa in om.acesso_s1.all():
            om.acesso_s1.remove(militar.pessoa)
        if militar.pessoa in om.acesso_s2.all():
            om.acesso_s2.remove(militar.pessoa)
        if militar.pessoa in om.acesso_s4.all():
            om.acesso_s4.remove(militar.pessoa)
        om.save()
    elif funcao == "aux_s4":
        om.acesso_s4.add(militar.pessoa)
        if militar.pessoa in om.acesso_s1.all():
            om.acesso_s1.remove(militar.pessoa)
        if militar.pessoa in om.acesso_s2.all():
            om.acesso_s2.remove(militar.pessoa)
        if militar.pessoa in om.acesso_s3.all():
            om.acesso_s3.remove(militar.pessoa)
        om.save()
    else:
        pass


def acesso_su(id_mil, funcao):
    militar = Militar.objects.get(id=id_mil)
    su = militar.subunidade
    if funcao == "cmt_su":
        su.cmt = militar.pessoa
        su.save()
    elif funcao == "sgte":
        su.sgte = militar.pessoa
        su.save()
    elif funcao == "enc_mat":
        su.enc_mat = militar.pessoa
        su.save()
    elif funcao == "aux_sgte":
        su.acesso_sgte.add(militar.pessoa)
        if militar.pessoa in su.acesso_encmat.all():
            su.acesso_encmat.remove(militar.pessoa)
        su.save()
    elif funcao == "aux_enc_mat":
        su.acesso_encmat.add(militar.pessoa)
        if militar.pessoa in su.acesso_sgte.all():
            su.acesso_sgte.remove(militar.pessoa)
        su.save()
    elif funcao == "ten_su":
        su.oficiais.add(militar.pessoa)
        su.quadros.add(militar.pessoa)
        su.save()
    elif funcao == "sgt_su":
        su.quadros.add(militar.pessoa)
        su.save()
    else:
        pass

