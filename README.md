# netappkr_AWSCDK
CDK 코드 저장 및 공유

## 사용 방법
- ```main_stack.py```의 스택 부분에 필요한 항목 추가
- Dependency 와 Parameter 확인 필수

> ### 주의!
> 개발자는 아니라서 코딩을 배운적은 없고.. 그저 IaC로 반복 좀 줄일려고 삽질하니 코드가 개판입니다.
> 부디 참고용으로만 봐주세요...

### 예시
```python
        # stack
        NW = NetworkStack(self, "NetworkStack", prefix=prefix)
        Tags.of(NW).add("creator", creator.value_as_string)

        BlueXP = BlueXPReqStack(self, "BlueXPReqStack", prefix=prefix)
        Tags.of(BlueXP).add("creator", creator.value_as_string)

        AD = ADStack(self, "ADStack", vpc=NW.vpc, prefix=prefix)
        Tags.of(AD).add("creator", creator.value_as_string)
        AD.add_dependency(NW)

        bastionhost = BastionStack(self, "BastionStack", vpc=NW.vpc, defaultsg=NW.defaultsg, prefix=prefix)
        Tags.of(bastionhost).add("creator", creator.value_as_string)
        bastionhost.add_dependency(NW)

        FSxN = FSxNStack(self, "FSxNStack", vpc=NW.vpc, AD=AD.cfn_microsoft_AD, defaultsg=NW.defaultsg, prefix=prefix)
        Tags.of(FSxN).add("creator", creator.value_as_string)
        FSxN.add_dependency(AD)
```

