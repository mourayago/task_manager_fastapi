# from sqlalchemy import create_engine, select
from sqlalchemy import select

# from sqlalchemy.orm import Session
from fast_zero.models import User


def test_create_user(session):
    # instancias abaixo rodando no conftest

    # # engine = create_engine('sqlite:///database.db')

    # # teste rodando em memória em um arquivo de db temporário
    # engine = create_engine('sqlite:///:memory:')

    # # Cria toda a estrutura do banco no teste
    # table_registry.metadata.create_all(engine)

    # # tudo que estiver acontecendo aqui vai acontecer na sessão
    # with Session(engine) as session:

    user = User(username='yago', email='yago@teste.com', password='senha@-123')
    session.add(user)
    session.commit()
    session.refresh(user)  # atualiza a tabela

    result = session.scalar(select(User).where(User.email == 'yago@teste.com'))

    assert result.username == 'yago'
